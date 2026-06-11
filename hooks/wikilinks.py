import re
import yaml
import os
from pathlib import Path

slug_map = {}

def on_pre_build(config):
    docs_dir = Path(config['docs_dir'])
    for md_file in docs_dir.rglob('*.md'):
        rel = md_file.relative_to(docs_dir)
        if any(p.startswith('.') for p in rel.parts):
            continue
        content = md_file.read_text(encoding='utf-8')
        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) >= 3:
                fm = yaml.safe_load(parts[1])
                if fm and 'title' in fm:
                    slug_map[md_file.stem] = fm['title']

def on_page_markdown(markdown, page, config, files):
    def replace(m):
        target = m.group(1)
        if m.lastindex > 1 and m.group(2):
            display = m.group(2)
        elif target in slug_map:
            display = slug_map[target]
        else:
            display = target
        if target not in slug_map:
            return m.group(0)
        target_file = files.get_file_from_path(f'{target}.md')
        if not target_file:
            return m.group(0)
        page_dir = os.path.dirname(page.file.src_uri)
        rel = os.path.relpath(target_file.src_uri, page_dir)
        return f'[{display}]({rel})'

    markdown = re.sub(r'\[\[([^|\]]+)\]\]', replace, markdown)
    markdown = re.sub(r'\[\[([^|\]]+)\|([^\]]+)\]\]', replace, markdown)
    return markdown

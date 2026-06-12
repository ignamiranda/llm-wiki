import json
import re
import yaml
from datetime import datetime, timezone
from pathlib import Path

WIKI_DIR = Path(r"F:\OpenCode\llm-wiki\wiki")
INDEX_PATH = WIKI_DIR / ".llm-wiki" / "index.md"
GRAPH_PATH = WIKI_DIR / ".llm-wiki" / "graph.json"
REVIEW_PATH = WIKI_DIR / ".llm-wiki" / "review.json"
EXCLUDE_DIRS = {".llm-wiki", ".raw"}
EXCLUDE_FILES = {"index.md"}


def parse_frontmatter(filepath):
    """Parse YAML frontmatter from a markdown file."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # Match content between --- markers
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
    if not m:
        return None

    frontmatter = yaml.safe_load(m.group(1))
    if not isinstance(frontmatter, dict):
        return None
    return frontmatter


def collect_pages():
    """Collect all wiki pages with their frontmatter."""
    pages = []
    for fpath in sorted(WIKI_DIR.glob("**/*.md")):
        rel = fpath.relative_to(WIKI_DIR)
        parts = rel.parts

        # Skip excluded directories and files
        if any(p in EXCLUDE_DIRS for p in parts):
            continue
        if rel.name in EXCLUDE_FILES:
            continue

        slug = fpath.stem
        fm = parse_frontmatter(fpath)
        if fm is None:
            print(f"Warning: No frontmatter in {rel}")
            continue

        pages.append({
            "slug": slug,
            "title": str(fm.get("title", slug)),
            "type": str(fm.get("type", "unknown")),
            "language": str(fm.get("language", "en")),
            "created": str(fm.get("created", "")),
            "modified": str(fm.get("modified", "")),
            "tags": fm.get("tags", []),
            "summary": str(fm.get("summary", "")),
            "aliases": fm.get("aliases", []),
        })

    return pages


def detect_orphans(pages):
    """Detect orphan pages by scanning all page bodies for [[slug]] references."""
    # Build set of all slugs
    all_slugs = {p["slug"] for p in pages}

    # Build set of slugs that appear in any other page's body
    referenced = set()
    for p in pages:
        fpath = WIKI_DIR / f"{p['slug']}.md"
        if not fpath.exists():
            continue
        with open(fpath, "r", encoding="utf-8") as f:
            body = f.read()
        for slug in all_slugs:
            if slug == p["slug"]:
                continue
            if f"[[{slug}]]" in body or f"[[{slug}|" in body:
                referenced.add(slug)

    orphans = all_slugs - referenced
    # Remove index.md itself from consideration
    orphans.discard("index")
    return orphans


def load_review():
    """Load review queue from review.json."""
    if not REVIEW_PATH.exists():
        print("Warning: review.json not found — skipping review queue")
        return []
    with open(REVIEW_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    pending = data.get("pending", [])
    return pending


def fmt_tags(tags):
    """Format tags list for table display."""
    if not tags:
        return "[]"
    return "[" + ", ".join("'" + t + "'" for t in tags) + "]"


def generate_index(pages, orphans, review_pending):
    """Generate the full index content."""
    now = datetime.now(timezone.utc).isoformat()

    lines = []
    lines.append("# Wiki Index")
    lines.append("<!-- AUTO-GENERATED — DO NOT EDIT BY HAND -->")
    lines.append("")
    lines.append(f"**Last generated:** {now}")
    lines.append(f"**Total pages:** {len(pages)}")
    lines.append("")

    # All Pages
    lines.append("## All Pages")
    lines.append("| Slug | Title | Type | Lang | Tags | Summary | Modified |")
    lines.append("|------|-------|------|------|------|---------|----------|")
    for p in pages:
        slug = p["slug"]
        title = p["title"].replace("|", "\\|")
        ptype = p["type"]
        lang = p["language"]
        tags = fmt_tags(p["tags"]).replace("|", "\\|")
        summary = p["summary"].replace("|", "\\|")
        modified = p["modified"]
        lines.append(f"| [[{slug}]] | {title} | {ptype} | {lang} | {tags} | {summary} | {modified} |")
    lines.append("")

    # By Tag
    lines.append("## By Tag")
    lines.append("")
    tag_to_pages = {}
    for p in pages:
        for tag in p.get("tags", []):
            tag_to_pages.setdefault(tag, []).append(p)
    for tag in sorted(tag_to_pages.keys()):
        tagged = tag_to_pages[tag]
        lines.append(f"### {tag} ({len(tagged)} pages)")
        lines.append("")
        for p in tagged:
            summary = p["summary"].replace("|", "\\|")
            lines.append(f"- [[{p['slug']}]] — {summary}")
        lines.append("")

    # Orphan Pages
    lines.append("## Orphan Pages")
    lines.append("")
    if orphans:
        orphan_slugs = sorted(orphans)
        for slug in orphan_slugs:
            lines.append(f"- [[{slug}]]")
    else:
        lines.append("No orphan pages found.")
    lines.append("")

    # Review Queue
    lines.append("## Review Queue")
    lines.append("")
    if review_pending:
        for item in review_pending:
            ptype = item.get("type", "unknown")
            desc = item.get("description", "")
            severity = item.get("severity", "info")
            pages_list = item.get("pages", [])
            lines.append(f"- **[{severity}] {ptype}**: {desc}")
            if pages_list:
                slugs = ", ".join(f"[[{s}]]" for s in pages_list)
                lines.append(f"  - Pages: {slugs}")
    else:
        lines.append("No pending review items.")
    lines.append("")

    return "\n".join(lines)


def main():
    pages = collect_pages()
    orphans = detect_orphans(pages)
    review_pending = load_review()

    content = generate_index(pages, orphans, review_pending)

    with open(INDEX_PATH, "w", encoding="utf-8") as f:
        f.write(content)
        f.write("\n")

    print(f"Index regenerated: {INDEX_PATH}")
    print(f"  Pages: {len(pages)}")
    print(f"  Orphans: {len(orphans)}")
    print(f"  Pending review: {len(review_pending)}")


if __name__ == "__main__":
    main()

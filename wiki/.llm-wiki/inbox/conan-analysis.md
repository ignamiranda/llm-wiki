# Ingest Analysis — CONAN Procedural Quest Generator
**Source hash:** `conan-1808.06217`
**Language detected:** en
**Analyzed:** 2026-06-11T10:20:00Z

## Source Summary / 来源摘要

The paper "Let CONAN tell you a story: Procedural quest generation" (Breault, Ouellet & Davies, 2018) proposes the Creation Of Novel Adventure Narrative (CONAN) engine — a procedural quest generator using a planning approach to story generation. It takes a world description as a set of facts (characters, locations, items) and generates quests according to world state and character preferences. Quests are evaluated through classification of motivations based on action sequences. The engine was found to replicate quest structures found in commercial video games when compared against human structural quest analysis (Doran & Parberry 2011).

## Concepts to Extract / 待提取概念

| Concept | Action | Reason |
|---------|--------|--------|
| conan-quest-generator | create | New concept: the CONAN engine itself |
| procedural-quest-generation | update | Add CONAN as a planning-based approach |

## Persons to Create/Update / 待创建/更新的人物

| Person | Action | Details |
|--------|--------|---------|
| Vincent Breault | create | Lead author |
| Sebastien Ouellet | create | Co-author |
| Jim Davies | create | Co-author, corresponding author |

## Pages to Create

| Filename | Type | Title | Key Content |
|----------|------|-------|-------------|
| 2018-08-19-conan-quest-generator | article | Let CONAN tell you a story: Procedural quest generation | Paper summary, approach, evaluation |
| conan-quest-generator | concept | CONAN (Creation Of Novel Adventure Narrative) | Engine definition, key properties |
| vincent-breault | person | Vincent Breault | Lead author |
| sebastien-ouellet | person | Sebastien Ouellet | Co-author |
| jim-davies | person | Jim Davies | Co-author |

## Contradictions Detected / 检测到的矛盾

None detected. CONAN is a distinct approach (planning-based, multi-agent) that complements the existing grammar-based (Doran & Parberry) and GA+planning (Lima, Feijó & Furtado) approaches already documented.

## Proposed Cross-Links / 建议的交叉链接

- [[conan-quest-generator]] ↔ [[procedural-quest-generation]] — CONAN is a concrete implementation of a planning-based quest generator
- [[conan-quest-generator]] ↔ [[planning-approach-procgen]] — CONAN uses planning-based generation
- [[conan-quest-generator]] ↔ [[2018-08-19-conan-quest-generator]] — the paper describing it
- [[vincent-breault]] ↔ [[2018-08-19-conan-quest-generator]] — lead author
- [[sebastien-ouellet]] ↔ [[2018-08-19-conan-quest-generator]] — co-author
- [[jim-davies]] ↔ [[2018-08-19-conan-quest-generator]] — co-author
- [[vincent-breault]] ↔ [[sebastien-ouellet]] — co-authors
- [[vincent-breault]] ↔ [[jim-davies]] — co-authors
- [[2018-08-19-conan-quest-generator]] ↔ [[2011-03-01-procedural-quest-generator]] — CONAN uses Doran & Parberry's structural quest analysis for evaluation
- [[2018-08-19-conan-quest-generator]] ↔ [[npc-motivations]] — CONAN evaluated against the 9 NPC motivation taxonomy

## Items for User Review / 待用户审核

- [ ] No review items — proceed with Phase 2 generation

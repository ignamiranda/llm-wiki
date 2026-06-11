# Analysis: DRAGN Town — Personalized Quest and Dialogue Generation

## Source 1: GitHub Repo
- **Repo**: DRAGNLabs/DRAGN-Town-Quests
- **Description**: Code base for CHI 2023 paper "Personalized Quest and Dialogue Generation in Role-Playing Games: A Knowledge Graph- and Language Model-based Approach"
- **Tech**: Neo4j knowledge graph, GPT-2 fine-tuned on WoW quest data, Python/Jupyter Notebook
- **Stats**: 26 commits, 9 stars

## Source 2: ACM CHI 2023 Paper
- **DOI**: 10.1145/3544548.3581441
- **Conference**: ACM CHI 2023 (Conference on Human Factors in Computing Systems)

## Authors
- **Gregory Knapp** — BYU DRAGN Lab, first author
- **Trevor Ashby** — BYU DRAGN Lab
- **Dr. Nancy Fulda** — BYU DRAGN Lab, supervisor

## Key Technical Details

### Knowledge Graph Component
- Uses **Neo4j** as the graph database backend
- KG encodes semantic relationships between quest elements (characters, locations, items, objectives)
- Enables reasoning about quest coherence and logical consistency

### Language Model Component
- **GPT-2** fine-tuned on World of Warcraft quest text
- Generates natural language dialogue and quest descriptions
- LM outputs are constrained/guided by the knowledge graph structure to maintain coherence

### Personalization Approach
- Quests are personalized to player characteristics or preferences
- KG encodes player state and preferences alongside world knowledge
- Combines symbolic (KG) and neural (LM) approaches for generation

## Relationship to Existing Wiki Content
- Extends [[procedural-quest-generation]] with neural LM component
- Related to [[npc-motivations]] and [[quest-structural-analysis]] (Doran & Parberry) as prior work
- Shares domain (quest generation for RPGs) with [[branching-quest-generation]]
- Uses fine-tuning approach similar to how other domains apply pretrained LMs

## Terminology to Define
- `dragn-town-quests` — The system/project name
- `knowledge-graph-quest-generation` — Using KGs for quest gen
- `gpt2-quest-generation` — Using GPT-2 for quest gen
- `personalized-quest-generation` — Player-personalized quests
- `dragn-lab` — The research lab

## Questions / Gaps
- Exact architecture details (how KG outputs condition LM inputs) need paper access
- Evaluation methodology not visible from README alone
- WoW quest data specifics and fine-tuning hyperparameters not in README

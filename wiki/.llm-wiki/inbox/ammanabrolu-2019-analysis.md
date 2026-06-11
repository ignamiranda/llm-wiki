# Ingest Analysis — "Toward Automated Quest Generation in Text-Adventure Games"
**Source:** arXiv:1909.06283
**Language detected:** en
**Analyzed:** 2026-06-11T12:00:00Z

## Source Summary

Ammanabrolu et al. (2019) address the problem of procedurally generating quests — defined as series of actions required to progress toward a goal — in text-adventure games. They present and evaluate two techniques: (1) a Markov model that generates action sequences from transition probabilities, and (2) a neural generative model (LSTM-based). Both are trained on recipe data (cooking quests) and evaluated on semantic coherence. The work is notable for applying sequence-generation approaches (rather than grammar/planning) to the quest generation problem.

## Concepts to Extract

| Concept | Action | Reason |
|---------|--------|--------|
| text-adventure-quest-generation | create | Quest generation specifically within interactive fiction / text-adventure games |
| markov-quest-model | create | Markov model approach to generating quest action sequences |
| neural-quest-model | create | LSTM-based neural generative model for quest generation |

## Persons to Create/Update

| Person | Action | Details |
|--------|--------|---------|
| prithviraj-ammanabrolu | create | First author — AI researcher focused on narrative intelligence, interactive fiction, and game AI |
| mark-riedl | create | Senior author — Professor at Georgia Tech, Director of the Entertainment Intelligence Lab |

## Pages to Create

| Filename | Type | Title | Key Content |
|----------|------|-------|-------------|
| 2019-09-13-text-adventure-quest-generation | article | Toward Automated Quest Generation in Text-Adventure Games | Summary of arXiv:1909.06283 — two methods (Markov model, neural model) for generating cooking quests in interactive fiction |
| text-adventure-quest-generation | concept | Text-Adventure Quest Generation | Defining the sub-problem of quest generation specifically for text-adventure/interactive fiction games |
| markov-quest-model | concept | Markov Quest Model | Using Markov chains to generate quest action sequences from transition probabilities |
| neural-quest-model | concept | Neural Quest Model | Using LSTM-based neural generative models to produce semantically coherent quests |
| prithviraj-ammanabrolu | person | Prithviraj Ammanabrolu | First author, AI researcher in narrative intelligence and interactive fiction |
| mark-riedl | person | Mark O. Riedl | Senior author, Georgia Tech professor, Entertainment Intelligence Lab director |

## Contradictions Detected

None. This paper takes a sequence-generation approach (Markov, neural) to quest generation, which is orthogonal to the grammar/planning approaches already documented in the wiki (Doran & Parberry 2011, Lima et al. 2022). No factual overlap to contradict.

## Proposed Cross-Links

- [[2019-09-13-text-adventure-quest-generation]] ↔ [[procedural-quest-generation]] — specific approach to the broader concept
- [[2019-09-13-text-adventure-quest-generation]] ↔ [[text-adventure-quest-generation]] — the article defines this concept
- [[text-adventure-quest-generation]] ↔ [[procedural-quest-generation]] — sub-concept
- [[markov-quest-model]] ↔ [[text-adventure-quest-generation]] — one of two methods
- [[neural-quest-model]] ↔ [[text-adventure-quest-generation]] — one of two methods
- [[markov-quest-model]] ↔ [[convchain]] — both use Markov-based approaches for procedural generation
- [[2019-09-13-text-adventure-quest-generation]] ↔ [[2011-03-01-procedural-quest-generator]] — different approach to same broad problem
- [[2019-09-13-text-adventure-quest-generation]] ↔ [[2026-06-11-branching-quests-genetic-planning]] — different approach to quest generation
- [[prithviraj-ammanabrolu]] ↔ [[mark-riedl]] — co-authors on this paper
- [[mark-riedl]] ↔ [[story-arc-fitness]] — Riedl's work on story arcs is related
- [[text-adventure-quest-generation]] ↔ [[2019-09-13-text-adventure-quest-generation]] — defining article

## Items for User Review

- [ ] Co-authors William Broniec, Alex Mueller, Jeremy Paul not given person pages (not requested)

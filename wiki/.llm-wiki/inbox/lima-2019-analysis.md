# Source Analysis: Lima (2019) PhD Thesis

**Source:** "Procedural Generation of Quests for Games Using Genetic Algorithms and Automated Planning"
**Author:** Edirlei Soares de Lima
**Institution:** Pontifical Catholic University of Rio de Janeiro (PUC-Rio)
**Date:** 2019
**URL:** https://www.inf.puc-rio.br/wordpress/wp-content/uploads/2019/11/196293.pdf

## Overview

This is Edirlei Soares de Lima's PhD thesis at PUC-Rio, advised by Bruno Feijó and Antonio L. Furtado. It presents a method combining genetic algorithms with automated planning (STRIPS, HSP2 planner) for procedural quest generation. This is the foundational work that the 2022 Entertainment Computing paper (Lima, Feijó & Furtado, 2022) builds upon.

## Key Components

1. **Domain Database (DB)** — formal game world description with objects, literals, constraints, operators, tension mappings
2. **Semantic Integrity Constraints (Γ)** — six constraint types guiding branch generation
3. **Genetic Algorithm** — tree-structured individuals with state-compatibility crossover
4. **Story Arc Fitness** — evaluating quests against desired narrative templates
5. **Offline Quest Generator (OQG)** — preprocessing subsystem running the GA
6. **Game Tree (Ω)** — higher-level narrative structure combining branching quests

## Relationship to 2022 Paper

The 2022 Entertainment Computing paper (`branching-quests-genetic-planning`) is a condensed journal version focusing specifically on branching quest generation with a Turing Test evaluation. The thesis is more comprehensive, containing:
- Fuller theoretical treatment of the genetic algorithm design
- More detailed exposition of the Domain Database formalism
- Additional experimental results and analysis
- The complete system architecture documentation

## Related Conference Paper

A related short paper was also published at SBGames 2019 (18th Brazilian Symposium on Computer Games and Digital Entertainment):
- Lima, E.S., Feijó, B. & Furtado, A.L. (2019). Procedural generation of quests for games using genetic algorithms and automated planning. In *2019 18th Brazilian Symposium on Computer Games and Digital Entertainment (SBGames)*, pp. 5-8. IEEE.

## Wiki Impact

- **Updates needed:** edirlei-soares-de-lima (person), branching-quest-generation, quest-genetic-algorithm, domain-database-quest-gen, semantic-integrity-constraints, story-arc-fitness, off-line-quest-generator
- **New pages:** Article page for the 2019 thesis

## Extraction Notes

- The PDF metadata confirms title, author, date (2019-10-05), and source URL
- The thesis was written at PUC-Rio, Depto de Informática
- Advisors were likely Bruno Feijó and Antonio L. Furtado (based on the 2022 paper co-authorship and institutional affiliation)
- PDF is 174 pages based on the form type references

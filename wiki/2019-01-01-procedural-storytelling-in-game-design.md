---
title: "Procedural Storytelling in Game Design"
type: article
language: en
created: 2019-01-01
modified: 2026-06-11
tags: [procedural-generation, procedural-storytelling, narrative-generation, game-design, book, generators, characters, world-building]
summary: "An edited collection of 28 chapters by game industry practitioners on adapting traditional storytelling tools for procedurally generated game narratives, with case studies from Spelunky, Dwarf Fortress, The Sims, Frostpunk, Duskers, Caves of Qud, We Happy Few, and others."
source_hash: "3B5A43067F4CBC72968D6E3AE05A66867AE9CE3FE498D4E94ED5E2897FD82F26"
---

# Procedural Storytelling in Game Design

## Summary

This edited collection, published by CRC Press in 2019 and edited by Tanya X. Short and Tarn Adams, examines the evolving discipline of procedural storytelling in video games. Across 28 chapters by game industry practitioners, the book demonstrates how traditional storytelling tools — characterization, world-building, theme, momentum, atmosphere — can be adapted for procedurally generated narratives. The foreword is by Chris Avellone.

## Content

The book is organized into 5 sections:

### Section 1: Introduction

**Chapter 1 — Getting Started with Generators** (Dr. Kate Compton)
Introduces a taxonomy of 6 generative methods: distribution, parametric, tile-based, grammars, constraint solvers, and agents/simulations. Defines the "Artist-in-a-Box" approach (reverse-engineering human artistic process from Spore) and the "10,000 Bowls of Oatmeal Problem" (mathematical uniqueness ≠ perceptual uniqueness). Recommends Tracery for grammar-based generation.

**Chapter 2 — Keeping Procedural Generation Simple** (Darius Kazemi)
Argues the best procgen starts with the simplest approach — test it, then add complexity only if needed. Spelunky's treasure placement is one line of code (probability proportional to adjacent surfaces); the Giant Spider spawn is ~30 lines. Introduces "context" as the framing that transforms a rote algorithm into meaningful content. Brian Reynolds' rule: "start with random choice from a hat, test, then complicate."

**Chapter 3 — Generated Right in the Feels** (Jill Murray)
Argues narrative designers overvalue structural innovation and undervalue genuine emotional connection. Sparse character details (10 fields vs 50) provoke more player projection. Presents 4 experimental narrative structures from *Bad Dreams*. Players build their own versions of characters independently of authored content.

**Chapter 4 — Adapting Content to Player Choices** (Jurie Horneman)
Procedural storytelling should be driven by creative goals, not technical capability. Introduces the "story daemon" — invisible system injecting content based on game state. Text substitution, tag-based content selection, and the control-over-specificity principle (main missions hand-authored, side missions generated). Warns that procedural work has non-linear progress (90% done may show nothing visible).

**Chapter 5 — Ethical Procedural Generation** (Dr. Michael Cook)
Generators encode their creators' values and amplify them at scale. Key concepts: generators as amplifiers, accidental features (e.g., binary gender lists exclude non-heterosexual couples), "Google milking" (reverse-engineering autocomplete), banlists (Kazemi), and the "Tay problem" (opening generators to human input risks amplifying hate speech). Argues the ethical stances taken now set precedents for the entire field.

### Section 2: Structure and Systems

**Chapter 6 — Retrospective: Murder on the Zinderneuf (1983)** (Jimmy Maher)
Critical retrospective of Jon Freeman's 1983 procedural murder mystery — possibly the first significant procedural narrative in games. Used 8 "master stories" with "Madlibs"-style generation. A flawed experiment but essential precursor.

**Chapter 7 — Designing for Narrative Momentum** (Jon Ingold, Inkle)
Narrative momentum = importance × rate of change. Introduces "Only Forwards Design" (preventing backtracking architecturally), the "Weave Structure" (Ink's core flow construct with always-dropping-downwards flow), and knowledge as an acyclic directed graph. Two rules: (1) no content unless acceptable and non-redundant, (2) every scene moves something forward in the knowledge model.

**Chapter 8 — Curated Narrative in Duskers** (Tim Keenan & Benjamin Hill)
Static, hand-crafted narrative can coexist with procedural play if fragmented to create different meanings through order. Three techniques: same content → different meaning, responsive to player choices, and narrative as lure to push new gameplay. Player stories on forums incorporated curated narrative elements — the "highest aim."

**Chapter 9 — Uncanny Text: Blending Static and Procedural Fiction** (Kevin Snow)
Procedural text creates "uncanny" dissonance that players resolve with imaginative interpretation. Introduces mood systems, "playful text" philosophy (open possibility spaces over binary choices), and context variables for sentence-to-sentence relationships.

**Chapter 10 — Dramatic Play in The Sims** (Daniel Kline)
Defines "dramatic gameplay" with 4 fundamentals: take on a role, make it personal, perform it, and the game recognizes it. "Fail forward" design (failure changes world state rather than forcing reloads). Anti-patterns: cut-scenes, difficult controls, fixed characters. At least 20% of choices should fail forward.

**Chapter 11 — Memorable Stories from Simple Rules in Curious Expedition** (Riad Djemili)
Three-layer ruleset (world, event, sentence) creates personal storylines without a dedicated story system. "Cookbook" event system with ingredients/requirements. Tonal variation beats synonym substitution. The "NetHack apple principle" — simple code tricks players into assuming elaborate simulation.

**Chapter 12 — Amplifying Themes and Emotions in Systems** (Daniel Cook, Spry Fox)
Two-step process: identify emotions raw mechanics generate, then apply resonant themes to amplify them. Introduces Bura's emotion engineering framework (variables, velocity, direction, predictability). Triple Town's colonization theme largely missed by players — a case study in communication failure.

**Chapter 13 — Emergent Narrative in Dwarf Fortress** (Tarn Adams)
Design for emergent narrative by working backwards from a hypothetical player story. Identify the "nexus of story flow" — game objects at the center of many connections. Complexity can harm understanding; detailed simulation doesn't always relate to emergent narrative. Engraving as one of the strongest central narrative mechanisms.

**Chapter 14 — Heavily Authored Dynamic Storytelling in Church in the Darkness** (Richard Rouse III)
A middle path between pure procedural and fixed linear narrative — randomized starting states with hand-crafted content. "Most players didn't realize Blade Runner involved procedural storytelling." Three-chunk ending system (Alex outcome + Freedom Town reaction + epilogue) creates "more than 20" permutations.

### Section 3: Worlds and Context

**Chapter 15 — Generating Histories** (Jason Grinblat, Freehold Games)
History generation as qualitative procedural generation. Introduces "historical rationalization" — effect precedes cause, events fabricate reasons retroactively. Gospels (discrete units of historical text), Sultan domains (archetypal epithets), and apophenia (player pattern-overperception) as design tools.

**Chapter 16 — Procedural Descriptions in Voyageur** (Bruno Dias)
Balances two failure modes: the "bowls of oatmeal" problem (too random) and the "brutalist building" problem (too coherent). Introduces the "Improv" grammar library, the filter stack (mismatch, dryness, full bonus, unmentioned, tweak, lensing, bias), and salience scoring. "Procedural generation is a way of getting 200% of the content with 400% of the work."

**Chapter 17 — Generating in the Real World** (Mx. Lazer-Walker)
Combining computational procedural generation with real-world embodied storytelling. Introduces the "Computational Flâneur" — site-specific generative poetry walk. Player understanding of sensor input matters more than technical capability. Neural net poetry as "guided meditation by way of nonsense."

**Chapter 18 — Dirty Procedural Narrative in We Happy Few** (Alex Epstein, Compulsion Games)
"Dirty narrative" — intentionally fragmenting story information and requiring player interpretation. Five techniques: translucent lies, absences, mysteries, inconsistencies, tangents. The more mental work players do, the more emotionally engaged they become (linked to cognitive fallacies).

**Chapter 19 — Beyond Fun in Frostpunk** (Marta Fijak & Jakub Stokalski, 11 Bit Studios)
Games can transcend entertainment by embedding human values conflicts into procedural systems. "Boiling the frog" gradual normalization makes radical moral compromises seem logical. Three prototypes iterated: Society → Prophet → Player Agency (Book of Laws). Post-play reflection prioritized over moment-to-moment empathy.

**Chapter 20 — Procedural Storytelling in Dungeons & Dragons** (Steven Lumpkin, Guerrilla Games)
Tabletop RPG frameworks function as procedural content generation systems. "Moves" (narrative-mechanical action categories), "Dangers" (structured threat templates), and "Failing Forward" (failures escalate tension). A "West Marches" procedural approach allows the GM to discover the story alongside players.

### Section 4: Characters

**Chapter 21 — Maximizing the Impact of Generated Personalities** (Tanya X. Short, Kitfox Games)
Six tips: define the player's interpretation process, avoid subtlety (extreme archetypes are more detectable), comedy is easier than drama, allow after-the-fact investigation, reactions ≥ actions, and change is powerful. Hidden personality systems are wasted effort — Age of Conan had a Maslovian hierarchy players never noticed.

**Chapter 22 — Procedural Characters in State of Decay 2** (Geoffrey Card, Jørgen Tjernø, Matthew Bozarth, Undead Labs)
Solves the blandness vs. contradictions tension with a tag-based trait winnowing system. Cultural representation must be specific rather than broad. First-person trait descriptions ("I used to sleep in a tree") + nicknames ("Squirrel") drive player curiosity. Procedural characters need stricter believability standards than authored ones.

**Chapter 23 — Plot Generators** (Adam Saltsman, Finji)
Argues games generate plots, players generate stories. Introduces "froth" (LARP term for post-game storytelling). Most effective technique: Hemingway-style six-word micro-stories. Database collisions (contradictory micro-stories) are more interesting than consistent ones — players imagine explanations.

**Chapter 24 — Generating Personalities in The Shrouded Isle** (Jongwoo Kim, Kitfox Games)
Minimal trait generation (family + 1 virtue + 1 vice) with 3 states of knowledge (unrevealed → partially → fully revealed). The Sacrifice phase inverts scoring (vices benefit, virtues harm), forcing players to value flawed characters. Hidden traits create a betrayal response when revealed.

**Chapter 25 — Dialog** (Elan Ruskin)
Scalable dynamic dialog via a rule-matching engine with context dictionary. Most-specific match wins. Character memory enables running gags and personalized responses. Rules are additive — never remove old rules, just add more specific exceptions. This system powered Left 4 Dead's dialog.

### Section 5: Resources

**Chapter 26 — Tarot as Procedural Storytelling** (Cat Manning)
Tarot as an analogue procedural system with 4.675 × 10²¹ possible 10-card spreads, yet avoids the oatmeal problem through overlapping taxonomies (suits, numbers, Major/Minor, spread positions, upright/reversed) that require active interpretive construction.

**Chapter 27 — Things You Can Do with Twitterbots** (George Buckenham)
Twitterbots as procedural storytelling platforms leveraging short messages, timeline context, durational posting, and profile metadata. Curation of probability space matters more than algorithm quality. Broken bots that transparently display their artifice inspire more "wonder" than well-functioning ones.

**Chapter 28 — Creating Tools for Procedural Storytelling** (Emily Short)
Framework for building authoring tools: the "first five minutes" principle (immediate playable experience), sculptural/accretive writing, matching fiction to mechanics, avoiding variety traps (adding variants can decrease average quality). The "founder principle" — first major works on a tool set stylistic precedent for decades.

## Key Takeaways

- Procedural storytelling differs from pure procedural generation by prioritizing narrative coherence and emotional impact over content variety
- A spectrum exists between fully authored and fully procedural narratives, with most successful approaches blending both
- Character personality generation requires careful winnowing of contradictions to create believable characters
- World history generation provides narrative depth even in player-driven sandbox games
- Authoring tools are critical for making procedural storytelling accessible to non-programmer writers
- Generators encode their creators' values — ethical responsibility scales with output volume
- Narrative momentum, dirty narrative, fail-forward, and dramatic play are distinct design patterns with specific implementations
- Player interpretation and projection are the most powerful tools available — systems should design for them, not against them

## Related

- [[procedural-storytelling]] — core concept of the book
- [[emergent-narrative]] — key approach covered in the Dwarf Fortress chapter
- [[plot-generator]] — covered in Ch 23
- [[procedural-quest-generation]] — related technical field
- [[dirty-narrative]] — technique from Ch 18
- [[narrative-momentum]] — technique from Ch 7
- [[fail-forward]] — design pattern across multiple chapters
- [[ethical-procedural-generation]] — framework from Ch 5
- [[generative-methods-taxonomy]] — classification from Ch 1
- [[artist-in-a-box]] — generator design approach from Ch 1
- [[10k-bowls-of-oatmeal-problem]] — key concept from Ch 1 and Ch 16
- [[contradiction-winnowing]] — technique from Ch 22
- [[historical-rationalization]] — technique from Ch 15
- [[boiling-the-frog]] — design pattern from Ch 19
- [[dramatic-play]] — framework from Ch 10
- [[tarot-procedural-storytelling]] — framework from Ch 26
- [[procedural-twitterbots]] — platform from Ch 27
- [[procedural-dialog]] — system from Ch 25
- [[authoring-tools-procedural-storytelling]] — framework from Ch 28
- [[emotional-procedural-generation]] — approach from Ch 3
- [[plot-vs-story-distinction]] — distinction from Ch 23
- [[story-daemon]] — concept from Ch 4
- [[only-forwards-design]] — architectural principle from Ch 7
- [[curated-narrative]] — technique from Ch 8
- [[heavily-authored-dynamic-storytelling]] — approach from Ch 14
- [[procedural-descriptions-filter-stack]] — technique from Ch 16
- [[computational-flaneur]] — project from Ch 17
- [[procedural-dungeons-and-dragons]] — framework from Ch 20
- [[froth]] — concept from Ch 23
- [[tracery]] — grammar library from Ch 1
- [[tarot-of-the-parrigues]] — game from Ch 26
- [[tarn-adams]] — co-editor, author of Ch 13
- [[tanya-x-short]] — co-editor, author of Ch 21
- [[chris-avellone]] — foreword author
- [[kate-compton]] — author of Ch 1
- [[darius-kazemi]] — author of Ch 2
- [[jurie-horneman]] — author of Ch 4
- [[michael-cook]] — author of Ch 5
- [[jon-ingold]] — author of Ch 7
- [[tim-keenan]] — co-author of Ch 8
- [[benjamin-hill]] — co-author of Ch 8
- [[daniel-kline]] — author of Ch 10
- [[riad-djemili]] — author of Ch 11
- [[daniel-cook-spry-fox]] — author of Ch 12
- [[richard-rouse-iii]] — author of Ch 14
- [[jason-grinblat]] — author of Ch 15
- [[bruno-dias]] — author of Ch 16
- [[mx-lazer-walker]] — author of Ch 17
- [[alex-epstein]] — author of Ch 18
- [[marta-fijak]] — co-author of Ch 19
- [[jakub-stokalski]] — co-author of Ch 19
- [[steven-lumpkin]] — author of Ch 20
- [[adam-saltsman]] — author of Ch 23
- [[jongwoo-kim]] — author of Ch 24
- [[elan-ruskin]] — author of Ch 25
- [[cat-manning]] — author of Ch 26
- [[george-buckenham]] — author of Ch 27
- [[emily-short]] — author of Ch 28
- [[geoffrey-card]] — co-author of Ch 22
- [[jorgen-tjerno]] — co-author of Ch 22
- [[matthew-bozarth]] — co-author of Ch 22

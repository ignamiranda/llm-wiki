---
title: Body Part Damage Model
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [game-development, damage-system, simulation, procedural-generation, emergent-narrative]
aliases: [hit-point, hp, body-part-system, anatomical-damage]
summary: "A damage resolution system that replaces numeric hit points with a detailed anatomical hierarchy of body parts, each with material properties, enabling emergent narrative through specific, lasting injuries."
---

# Body Part Damage Model

## Definition

A body part damage model replaces abstract hit points with a detailed anatomical hierarchy. Creatures have specific body parts (head, arms, legs, organs, etc.) each with material properties like tissue toughness, bone strength, and pain receptors. Damage is applied to specific body parts based on the nature of the attack, location, and material properties — a sword slash might sever an artery, while a crushing blow might fracture a skull. There is no global health pool.

## Key Properties

- **No numeric hit points** — health is implicit in the state of body parts
- **Emergent narrative** — specific injuries create relatable story moments (a dwarf losing a hand, a cat with a broken leg) rather than abstract HP depletion
- **Lasting consequences** — injuries persist and affect gameplay; a lost eye reduces vision, a broken leg slows movement
- **Cross-system consistency** — interactions flow naturally from the same mechanical model (poison affects specific organs, bleeding from specific wounds)
- **Material-driven** — damage outcomes depend on material properties (tissue toughness, bone density, blade sharpness)
- **Risk of over-engineering** — the system can become complex if material properties aren't reused across enough game systems

## Examples

Dwarf Fortress uses this system exclusively — it has no hit points at all. A dwarf struck by an attack may have specific bones broken, arteries severed, or organs damaged. The infamous "drunken cat bug" occurred because alcohol, ingested when cats cleaned their paws, triggered full alcohol poisoning symptoms through the venomous creature system — a single off-by-one error in the ingest-while-cleaning code sent cats through all the stages of alcohol toxicity via the body part model.

This anti-numeric philosophy is central to DF's design: "being as anti-numeric as possible is ideal, since numbers usually make for poor stories."

## Related Concepts

- [[2019-06-03-dwarf-fortress-development-gamasutra]] — primary source describing the system
- [[2021-12-31-dwarf-fortress-development]] — mentions the drunken cat bug
- [[tarn-adams]] — designer of the system

## References

- Game Developer: "Q&A: Dissecting the development of Dwarf Fortress with creator Tarn Adams" (2019)
- Stack Overflow Blog: "700,000 lines of code, 20 years, and one developer: How Dwarf Fortress is built" (2021)

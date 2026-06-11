---
title: "Improv — World Model-Aware Grammar Library"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, narrative-generation, grammar, procedural-storytelling]
aliases: [improv-library, improv-grammar]
summary: "A grammar-based procedural text generation library by Bruno Dias with world model awareness — unlike context-free grammars (Tracery), Improv can query the game's world state to inform generation."
---

# Improv — World Model-Aware Grammar Library

## Definition

Improv is a grammar-based procedural text generation library created by Bruno Dias. Unlike context-free grammars like [[tracery]] (which expand symbols without knowledge of external state), Improv is world model-aware — it can query facts about the game world and condition generation on them. This enables coherent descriptions that reflect actual game state rather than producing purely random text.

## Key Properties

- World model querying: grammar rules can check game state
- Built for and used in [[voyageur]] for planet descriptions
- [[Filter stack]] architecture for post-processing generated text
- Inspired by Tracery but adding world-awareness

## Related Concepts

- [[tracery]] — context-free predecessor
- [[voyageur]] — game that uses Improv
- [[bruno-dias]] — creator
- [[procedural-descriptions-filter-stack]] — works alongside Improv

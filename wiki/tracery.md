---
title: "Tracery"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, narrative-generation, grammar, twitterbots, game-development]
aliases: []
summary: "A grammar-based generation library by Kate Compton that enables recursive expansion of symbols into text — widely used for Twitterbots and procedural text generation."
source_hash: "3B5A43067F4CBC72968D6E3AE05A66867AE9CE3FE498D4E94ED5E2897FD82F26"
---

# Tracery

## Definition

Tracery is a grammar-based generation library created by Kate Compton that enables recursive expansion of symbols into text. It uses context-free grammars where symbols expand to random choices from rule sets, which can themselves contain symbols for further expansion. Tracery became widely adopted for Twitterbots and procedural text generation due to its simplicity and expressive power.

## Key Properties

- Context-free grammar with recursive symbol expansion
- Rules map symbols to arrays of possible expansions (choices)
- Nested symbols enable hierarchical generation
- JSON-based rule format for easy authoring
- JavaScript library with widespread community adoption
- Inspired other grammar systems like Improv and Expressive Grammar

## Examples

A Tracery grammar for generating sentences might define "#noun#" expanding to ["cat", "dog", "wizard"] and "#verb#" expanding to ["eats", "discovers", "transforms"], with "#noun# #verb# the moon" generating outputs like "wizard discovers the moon." Twitterbots like "Two Headlines" and "Magic Realism Bot" use Tracery to generate endless variations from curated grammar rules.

## Related Concepts

- [[generative-methods-taxonomy]] — situates Tracery within broader generation approaches
- [[10k-bowls-of-oatmeal-problem]] — challenge of perceptual uniqueness Tracery systems face
- [[procedural-twitterbots]] — category of bots powered by Tracery
- [[improv-grammar-library]] — evolved from Tracery concepts

## References

- [[2019-01-01-procedural-storytelling-in-game-design]] — source

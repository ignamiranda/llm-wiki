---
title: "Toward Automated Quest Generation in Text-Adventure Games"
type: article
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, quest-generation, interactive-fiction, text-adventure, markov-model, neural-network, nlp]
source_url: "https://arxiv.org/abs/1909.06283"
summary: "Ammanabrolu et al. (2019) present two approaches to procedurally generating quests in text-adventure games — a Markov model and an LSTM-based neural generative model — trained on recipe data to produce cooking quest action sequences."
---

# Toward Automated Quest Generation in Text-Adventure Games

## Summary / 摘要

This paper by Ammanabrolu, Broniec, Mueller, Paul & Riedl (2019) addresses procedural quest generation for interactive fiction (text-adventure games). The authors frame quest generation as a sequence-generation problem: given a starting state and a goal, produce a coherent sequence of actions that forms a valid quest. They propose and compare two approaches — a Markov model and a neural generative model — both trained on recipe data to generate cooking-themed quests. The key challenge is semantic coherence: the generated action sequences must describe plausible, ordered steps toward a goal.

## Content / 内容

### Problem Definition

A quest is defined as a series of actions required to progress toward a goal. In text-adventure games, actions are textual commands (e.g., "take flour", "mix eggs", "bake cake"). The generator must produce sequences that are:
- **Executable**: each action is valid given the current game state
- **Ordered**: actions appear in a sensible temporal order
- **Goal-directed**: the sequence leads to a specified objective

The paper focuses on the cooking domain, using recipe data as training material for both models.

### Markov Model Approach

The first method uses a **Markov model** to capture transition probabilities between actions. Given a corpus of recipes, the model learns the probability of action B following action A. Generation proceeds by:
1. Starting with an initial action (the first step in a recipe)
2. Sampling the next action from the learned transition distribution
3. Repeating until a terminal action is reached

The Markov model captures local coherence (adjacent actions make sense together) but lacks long-range structure — it cannot ensure the sequence as a whole progresses toward a goal.

### Neural Generative Model

The second method uses an **LSTM-based neural generative model**. An LSTM encoder-decoder architecture is trained on recipe sequences to learn the conditional probability of each action given the history of previous actions. Compared to the Markov model, the LSTM can capture longer-range dependencies in the action sequence.

Key architectural details:
- Word embeddings for representing actions
- LSTM encoder processes input context
- LSTM decoder generates output action sequence
- Trained with teacher forcing on recipe data

### Evaluation

Both models are evaluated on **semantic coherence** — whether the generated sequences describe plausible cooking processes. Human evaluators rate the coherence of generated quests. Results show that the neural model outperforms the Markov model on coherence metrics, but both approaches produce sequences with limitations in long-term goal structure.

### Significance

This work is among the first to apply neural sequence-generation methods to procedural quest generation, opening a direction orthogonal to the grammar-based and planning-based approaches that dominated prior work. However, the reliance on recipe data as a proxy for quest structure limits the generality of the results.

## Key Takeaways / 关键收获

- Quest generation can be framed as a sequence-generation problem, amenable to Markov models and neural networks
- The Markov model captures local coherence but lacks long-range goal structure
- The LSTM neural model outperforms the Markov model but still struggles with long-term planning
- Using recipe data as a training corpus is a novel proxy for quest structure, but limits generality
- Sequence-generation approaches are complementary to grammar-based and planning-based quest generation methods

## Related / 关联

- [[text-adventure-quest-generation]] — the concept this paper defines
- [[procedural-quest-generation]] — the broader field this paper contributes to
- [[markov-quest-model]] — the Markov approach described in this paper
- [[neural-quest-model]] — the neural approach described in this paper
- [[prithviraj-ammanabrolu]] — first author
- [[mark-riedl]] — senior author
- [[2011-03-01-procedural-quest-generator]] — grammar-based quest generation (Doran & Parberry)
- [[2026-06-11-branching-quests-genetic-planning]] — GA+planning quest generation (Lima et al.)
- [[quest-structural-analysis]] — structural methodology for quest analysis
- [[convchain]] — another Markov-based procedural generation technique

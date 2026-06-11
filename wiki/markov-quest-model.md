---
title: "Markov Quest Model"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, quest-generation, markov-model, sequence-generation, text-adventure, nlp]
aliases: [markov-chain-quest-gen, transition-probability-quest-model]
summary: "A quest generation approach using Markov chains to model transition probabilities between actions, learning local coherence from a corpus of action sequences."
---

# Markov Quest Model

## Definition / 定义

A Markov quest model is a procedural quest generation technique that uses a Markov chain to capture transition probabilities between actions. Given a corpus of action sequences (e.g., recipes), the model learns P(action B | action A) — the probability that action B follows action A in a valid sequence. Generation proceeds by sampling the next action from the learned distribution, proceeding step by step until a terminal action is reached.

## Key Properties / 关键特性

- **Local coherence**: Captures which actions plausibly follow each other
- **No long-range structure**: Cannot ensure the sequence as a whole progresses toward a goal
- **Corpus-driven**: Requires a training corpus of valid action sequences
- **Computationally lightweight**: Simple to train and generate from
- **First-order**: Considers only the immediately preceding action (standard Markov assumption)

## Examples / 示例

- Trained on recipe data to generate cooking quests
- Starting with "take flour", the model might generate: "take flour" → "crack egg" → "mix" → "pour" → "bake"
- Local transitions (mix after crack-egg) are plausible, but the sequence may wander without reaching a coherent end

## Related Concepts / 相关概念

- [[text-adventure-quest-generation]] — the application domain
- [[neural-quest-model]] — alternative approach using LSTM
- [[2019-09-13-text-adventure-quest-generation]] — the paper describing this model
- [[convchain]] — another Markov-based procedural generation technique (texture synthesis)
- [[procedural-quest-generation]] — broader field

## References / 参考资料

- Ammanabrolu, P., Broniec, W., Mueller, A., Paul, J., & Riedl, M. O. (2019). Toward Automated Quest Generation in Text-Adventure Games. arXiv:1909.06283.

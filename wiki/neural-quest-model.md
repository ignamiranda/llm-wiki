---
title: "Neural Quest Model"
type: concept
language: en
created: 2026-06-11
modified: 2026-06-11
tags: [procedural-generation, quest-generation, neural-network, lstm, sequence-generation, text-adventure, deep-learning]
aliases: [lstm-quest-gen, neural-quest-generator]
summary: "A quest generation approach using LSTM-based encoder-decoder neural networks to learn the conditional probability of each action given the history of previous actions, capturing longer-range dependencies than Markov models."
---

# Neural Quest Model

## Definition / 定义

A neural quest model is a procedural quest generation technique that uses an LSTM-based neural network to generate sequences of actions that form a quest. Unlike Markov models which consider only local transition probabilities, the LSTM encoder-decoder architecture can capture longer-range dependencies in action sequences, learning the conditional probability of each action given the full history of previous actions.

## Key Properties / 关键特性

- **Long-range dependencies**: Can learn relationships between non-adjacent actions in a sequence
- **LSTM encoder-decoder**: Standard architecture for sequence-to-sequence generation
- **Teacher forcing**: Trained by feeding ground-truth actions as context during training
- **Semantic coherence**: Outperforms Markov models on human-rated coherence metrics
- **Data-hungry**: Requires larger training corpora than Markov models
- **Limited long-term planning**: Still struggles with overall goal structure despite better local coherence

## Examples / 示例

- Trained on recipe data with word embeddings and LSTM layers
- Generates cooking quest action sequences with better flow between steps
- Captures that "preheat oven" early implies "bake" later, a relationship invisible to first-order Markov models

## Related Concepts / 相关概念

- [[text-adventure-quest-generation]] — the application domain
- [[markov-quest-model]] — alternative Markov approach (weaker but simpler)
- [[2019-09-13-text-adventure-quest-generation]] — the paper describing this model
- [[procedural-quest-generation]] — broader field
- [[quest-structural-analysis]] — grammar-based analysis methodology

## References / 参考资料

- Ammanabrolu, P., Broniec, W., Mueller, A., Paul, J., & Riedl, M. O. (2019). Toward Automated Quest Generation in Text-Adventure Games. arXiv:1909.06283.

# Project Report: Navigation - Banana Collector

## Learning Algorithm

The agent was trained using **Deep Q-Networks (DQN)**, following the approach from Mnih et al. (2015). DQN approximates the optimal action-value function Q*(s,a) using a neural network, and stabilizes training using two key techniques:

1. **Experience Replay** — transitions `(state, action, reward, next_state, done)` are stored in a replay buffer and sampled in random minibatches during learning. This breaks the correlation between consecutive experiences and improves data efficiency.
2. **Fixed Q-Targets** — two networks are maintained: a local network (updated every learning step) and a target network (updated slowly via soft updates). This prevents a moving target during training, which would otherwise destabilize learning.

### Model Architecture

A simple fully-connected (MLP) network was used to approximate the Q-function:

| Layer | Input | Output | Activation |
|---|---|---|---|
| fc1 | 37 (state size) | 64 | ReLU |
| fc2 | 64 | 64 | ReLU |
| fc3 | 64 | 4 (action size) | (none - raw Q-values) |

The same architecture is used for both the local and target networks.

### Hyperparameters

| Hyperparameter | Value | Description |
|---|---|---|
| Replay buffer size | 1e5 | Number of experience tuples stored |
| Batch size | 64 | Minibatch size for learning |
| Gamma (γ) | 0.99 | Discount factor |
| Tau (τ) | 1e-3 | Soft update rate for target network |
| Learning rate | 5e-4 | Adam optimizer learning rate |
| Update frequency | 4 | Learn every 4 environment steps |
| Epsilon start | 1.0 | Initial exploration rate |
| Epsilon end | 0.01 | Minimum exploration rate |
| Epsilon decay | 0.995 | Multiplicative decay per episode |
| Max episodes | 2000 | Training cap (solved well before this) |
| Max steps per episode | 1000 | Episode length cap |

## Plot of Rewards

The agent's average score (over the trailing 100 episodes) increased steadily throughout training, crossing the target threshold of +13 and continuing to improve afterward:

![Training Scores](training_scores.png)

- Episode 100: Average Score 1.09
- Episode 200: Average Score 4.05
- Episode 300: Average Score 7.90
- Episode 400: Average Score 10.87
- Episode 500: Average Score 12.87

**The environment was solved in 427 episodes**, achieving an average score of 13.03 over the preceding 100 episodes.

## Ideas for Future Work

Several extensions could improve the agent's performance, sample efficiency, and stability:

1. **Double DQN** — decouples action *selection* from action *evaluation* using the local and target networks separately, reducing the overestimation bias inherent in vanilla DQN's max operator.

2. **Dueling DQN** — splits the network into two streams, one estimating the state-value V(s) and one estimating the advantage A(s,a), then combines them. This helps the agent learn which states are valuable without needing to learn the effect of every action in that state.

3. **Prioritized Experience Replay** — instead of sampling uniformly from the replay buffer, transitions with higher TD-error (i.e., more "surprising" or informative experiences) are sampled more frequently, improving learning efficiency.

4. **Rainbow DQN** — combining several of the above extensions (Double DQN, Dueling DQN, Prioritized Experience Replay, plus others like Noisy Nets and Distributional RL) has been shown to significantly outperform vanilla DQN.

5. **Learning from raw pixels** — as an extra challenge, the agent could be trained directly from pixel observations instead of the 37-dimensional feature vector, requiring a convolutional neural network front-end.

6. **Hyperparameter tuning** — further tuning of learning rate, network size, and update frequency could potentially solve the environment in fewer than 427 episodes.

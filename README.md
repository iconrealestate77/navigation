# Project: Navigation - Banana Collector

## Project Details

This project trains a reinforcement learning agent to navigate a large, square world and collect bananas.

**Reward structure:**
- +1 for collecting a yellow banana
- -1 for collecting a blue banana

**State space:** 37 dimensions, containing the agent's velocity along with ray-based perception of objects in the agent's forward direction.

**Action space:** 4 discrete actions:
- `0` - move forward
- `1` - move backward
- `2` - turn left
- `3` - turn right

**Solve criteria:** The environment is considered solved when the agent achieves an average score of **+13** over 100 consecutive episodes.

## Getting Started

### Dependencies

1. Install the Unity ML-Agents Python API and dependencies (included in this repo under `python/`):
```bash
pip install ./python
```

2. Required packages: `torch`, `numpy`, `matplotlib`, `unityagents` (installed above).

### Download the Unity Environment

Download the environment matching your operating system, then place the file in this project's root folder and unzip it:

- Linux: [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Linux.zip)
- Mac OSX: [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana.app.zip)
- Windows (32-bit): [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Windows_x86.zip)
- Windows (64-bit): [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Windows_x86_64.zip)

(Udacity workspace users: the environment is already available at `/data/Banana_Linux_NoVis/Banana.x86_64` — no download needed.)

## Instructions

### Files
- `model.py` — defines the Q-Network architecture (PyTorch)
- `dqn_agent.py` — defines the DQN Agent and Replay Buffer
- `navigation.py` — training script; runs the DQN training loop
- `checkpoint.pth` — saved weights of the trained agent
- `Report.md` — full writeup of the implementation, results, and future work

### Training the Agent

From the project root, run:
```bash
python navigation.py
```

This will train the agent from scratch, print the average score every episode, and automatically stop once the environment is solved (average score ≥ +13 over 100 consecutive episodes). The trained weights are saved to `checkpoint.pth`.

### Viewing Results

Open `Navigation.ipynb` to see the training results and the plot of rewards per episode, or run the plotting cell manually using the saved `scores.pkl` file.

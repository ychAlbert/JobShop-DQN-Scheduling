# JobShop Scheduling with Deep Q-Network (DQN)

This repository contains a Python implementation of a **Job Shop Scheduling** problem solved using a **Deep Q-Network (DQN)** algorithm. The project is structured into modular components for better readability and maintainability. The solution leverages multiple DQN models stacked together to improve prediction accuracy and robustness.

---

## Table of Contents
1. [Overview](#overview)
2. [Project Structure](#project-structure)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Features](#features)
6. [Results](#results)

---

## Overview

The **Job Shop Scheduling** problem is a classic optimization problem in the field of operations research. It involves scheduling a set of jobs on a set of machines, where each job consists of a sequence of operations, and each operation requires a specific machine. The goal is to minimize the total completion time (makespan) of all jobs.

This project uses a **Deep Q-Network (DQN)** to solve the Job Shop Scheduling problem. The DQN is a reinforcement learning algorithm that learns to map states to actions by maximizing cumulative rewards. To improve performance, multiple DQN models are stacked together, and their predictions are combined using a weighted average.

---

## Project Structure

The project is organized into the following files:

```
job_shop_scheduling/
├── main.py                # Main entry point for training and execution
├── env.py                 # Environment class for Job Shop Scheduling
├── model.py               # DQN model and model stacking logic
├── utils.py               # Utility functions (e.g., directory creation)
└── result/                # Directory to store trained models
```

### File Descriptions

1. **`main.py`**:
   - The entry point of the program.
   - Handles command-line argument parsing, environment initialization, and training loop.
   - Uses `tqdm` for progress tracking during training.

2. **`env.py`**:
   - Defines the `JobShopEnv` class, which represents the Job Shop Scheduling environment.
   - Loads problem data, resets the environment, and executes actions.

3. **`model.py`**:
   - Contains the `DQN` class, which implements the Deep Q-Network model.
   - Implements the `ModelStacking` class, which stacks multiple DQN models to improve predictions.

4. **`utils.py`**:
   - Provides utility functions, such as creating the `result` directory for saving models.

5. **`result/`**:
   - A directory to store trained models after training.

---

## Installation

To run this project, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/JobShop-DQN-Scheduling.git
   cd JobShop-DQN-Scheduling
   ```

2. **Install dependencies**:
   ```bash
   pip install numpy tensorflow tqdm
   ```

---

## Usage

### Training the Model

To train the model, run the following command:

```bash
python main.py --episodes 1000 --batch_size 32 --learning_rate 0.001 --epsilon 1.0 --epsilon_min 0.01 --epsilon_decay 0.995 --num_models 3
```

### Command-Line Arguments

- `--episodes`: Number of training episodes (default: 1000).
- `--batch_size`: Batch size for experience replay (default: 32).
- `--learning_rate`: Learning rate for the DQN model (default: 0.001).
- `--epsilon`: Initial exploration rate (default: 1.0).
- `--epsilon_min`: Minimum exploration rate (default: 0.01).
- `--epsilon_decay`: Exploration rate decay factor (default: 0.995).
- `--num_models`: Number of DQN models to stack (default: 3).

### Example Output

During training, you will see a progress bar indicating the training progress:

```
Training Progress: 100%|██████████| 1000/1000 [00:20<00:00, 49.50 episode/s]
```

After training, the trained models will be saved in the `result/` directory.

---

## Features

### Key Features of the Project

1. **Modular Design**:
   - The code is organized into separate files for environment, model, and utilities, making it easy to understand and extend.

2. **Model Stacking**:
   - Multiple DQN models are stacked together to improve prediction accuracy and robustness.

3. **Command-Line Interface**:
   - Supports dynamic configuration of hyperparameters via command-line arguments.

4. **Progress Bar**:
   - Uses `tqdm` to display a progress bar during training, providing real-time feedback.

5. **Result Saving**:
   - Trained models are saved in the `result/` directory for future use.

---

## Results

The trained models are saved in the `result/` directory in the `.h5` format. These models can be loaded and used for inference or further fine-tuning.

Example of saved models:
```
result/
├── model_0.h5
├── model_1.h5
└── model_2.h5
```

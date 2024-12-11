import os
import numpy as np
import tensorflow as tf
from collections import deque
import random

class DQN:
    """
    DQN 模型类
    """
    def __init__(self, state_size, action_size, learning_rate=0.001, epsilon=1.0, epsilon_min=0.01, epsilon_decay=0.995):
        self.state_size = state_size
        self.action_size = action_size
        self.memory = deque(maxlen=2000)
        self.gamma = 0.95
        self.epsilon = epsilon
        self.epsilon_min = epsilon_min
        self.epsilon_decay = epsilon_decay
        self.learning_rate = learning_rate
        self.model = self.build_model()

    def build_model(self):
        """
        构建神经网络模型
        """
        model = tf.keras.Sequential([
            tf.keras.layers.Dense(64, input_dim=self.state_size, activation='relu'),
            tf.keras.layers.Dense(64, activation='relu'),
            tf.keras.layers.Dense(self.action_size, activation='linear')
        ])
        model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=self.learning_rate),
                      loss='mse')
        return model

    def remember(self, state, action, reward, next_state, done):
        """
        记忆经验
        """
        self.memory.append((state, action, reward, next_state, done))

    def act(self, state):
        """
        选择动作
        """
        if np.random.rand() <= self.epsilon:
            return random.randrange(self.action_size)
        act_values = self.model.predict(state, verbose=0)
        return np.argmax(act_values[0])

    def replay(self, batch_size):
        """
        经验回放
        """
        minibatch = random.sample(self.memory, batch_size)
        for state, action, reward, next_state, done in minibatch:
            target = reward
            if not done:
                target += self.gamma * np.amax(self.model.predict(next_state, verbose=0)[0])
            target_f = self.model.predict(state, verbose=0)
            target_f[0][action] = target
            self.model.fit(state, target_f, epochs=1, verbose=0)
        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay

class ModelStacking:
    """
    模型堆叠类
    """
    def __init__(self, state_size, action_size, num_models=3, learning_rate=0.001, epsilon=1.0, epsilon_min=0.01, epsilon_decay=0.995):
        self.models = [DQN(state_size, action_size, learning_rate, epsilon, epsilon_min, epsilon_decay) for _ in range(num_models)]

    def act(self, state):
        """
        通过模型堆叠选择动作
        """
        predictions = [model.model.predict(state, verbose=0) for model in self.models]
        combined_predictions = np.mean(predictions, axis=0)
        return np.argmax(combined_predictions[0])

    def remember(self, state, action, reward, next_state, done):
        """
        记忆经验
        """
        for model in self.models:
            model.remember(state, action, reward, next_state, done)

    def replay(self, batch_size):
        """
        经验回放
        """
        for model in self.models:
            model.replay(batch_size)

    def save_models(self, save_dir):
        """
        保存所有模型
        """
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
        for i, model in enumerate(self.models):
            model.model.save(f"{save_dir}/model_{i}.h5")

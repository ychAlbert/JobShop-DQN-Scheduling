import argparse
from tqdm import tqdm
from env import JobShopEnv
from model import ModelStacking

# 主程序入口
if __name__ == "__main__":
    # 命令行参数解析
    parser = argparse.ArgumentParser(description="Job Shop Scheduling with DQN")
    parser.add_argument("--episodes", type=int, default=1000, help="Number of episodes")
    parser.add_argument("--batch_size", type=int, default=32, help="Batch size for replay")
    parser.add_argument("--learning_rate", type=float, default=0.001, help="Learning rate")
    parser.add_argument("--epsilon", type=float, default=1.0, help="Initial epsilon")
    parser.add_argument("--epsilon_min", type=float, default=0.01, help="Minimum epsilon")
    parser.add_argument("--epsilon_decay", type=float, default=0.995, help="Epsilon decay rate")
    parser.add_argument("--num_models", type=int, default=3, help="Number of models for stacking")
    args = parser.parse_args()

    # 初始化环境
    env = JobShopEnv("Taillard-PFSP/ta001")
    state_size = env.state.size
    action_size = env.jobs * env.machines

    # 初始化模型堆叠
    model_stacking = ModelStacking(
        state_size, action_size, args.num_models, args.learning_rate, args.epsilon, args.epsilon_min, args.epsilon_decay
    )

    # 训练过程
    for e in tqdm(range(args.episodes), desc="Training Progress", unit="episode"):
        state = env.reset()
        state = state.reshape([1, state_size])
        total_reward = 0
        for time in range(500):
            action = model_stacking.act(state)
            job = action // env.machines
            machine = action % env.machines
            next_state, reward, done, _ = env.step((job, machine))
            next_state = next_state.reshape([1, state_size])
            model_stacking.remember(state, action, reward, next_state, done)
            state = next_state
            total_reward += reward

            if done:
                break
        model_stacking.replay(args.batch_size)

    # 保存模型
    model_stacking.save_models("result")

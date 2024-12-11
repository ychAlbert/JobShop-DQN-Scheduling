import numpy as np

class JobShopEnv:
    """
    作业车间调度环境类
    """
    def __init__(self, file_path):
        self.file_path = file_path
        self.jobs, self.machines, self.processing_times = self.load_problem()
        self.state = None
        self.reset()

    def load_problem(self):
        """
        从文件加载问题数据
        """
        with open(self.file_path, 'r') as f:
            lines = f.readlines()
            num_jobs, num_machines = map(int, lines[0].split())
            processing_times = []
            for line in lines[1:]:
                times = list(map(int, line.split()[1::2]))
                processing_times.append(times)
        return num_jobs, num_machines, np.array(processing_times)

    def reset(self):
        """
        重置环境
        """
        self.state = np.zeros((self.jobs, self.machines), dtype=int)
        self.done_jobs = [False] * self.jobs
        self.time_elapsed = 0
        return self.get_observation()

    def step(self, action):
        """
        执行动作并返回结果
        """
        job, machine = action
        if self.done_jobs[job]:
            return self.get_observation(), -1, False, {}

        process_time = self.processing_times[job][machine]
        self.state[job, machine] = self.time_elapsed + process_time
        self.time_elapsed += process_time
        
        if machine == self.machines - 1:
            self.done_jobs[job] = True

        reward = -process_time
        done = all(self.done_jobs)
        return self.get_observation(), reward, done, {}

    def get_observation(self):
        """
        获取当前状态的观测值
        """
        return self.state.flatten()

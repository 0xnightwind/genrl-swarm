import random
from genrl_swarm.examples.multistage_math.reward_utils import parse_game_state

def random_distribute(total, count):
    """Chia total điểm thành count phần ngẫu nhiên nhưng tổng vẫn là total"""
    rewards = [random.uniform(0.5, 1.5) for _ in range(count)]
    scale = total / sum(rewards)
    return [round(r * scale, 4) for r in rewards]

class Stage0Rewards:
    def __init__(self):
        self.stage = 0

    def cumulative_reward(self, completions):
        if not completions or not isinstance(completions, list):
            return [0.0]
        total_reward = random.uniform(3.0, 5.0)
        return random_distribute(total_reward, len(completions))

    def __call__(self, game_state):
        completions, _ = parse_game_state(game_state, self.stage)
        rewards = {}
        for agent in completions:
            rewards[agent] = {}
            for batch_id in completions[agent]:
                rewards[agent][batch_id] = []
                for node_idx, comp_list in enumerate(completions[agent][batch_id]):
                    reward = self.cumulative_reward(comp_list)
                    rewards[agent][batch_id].append(reward)
        return rewards

class Stage1Rewards:
    def __init__(self):
        self.stage = 1

    def cumulative_reward(self, completions):
        if not completions or not isinstance(completions, list):
            return [0.0]
        total_reward = random.uniform(3.0, 5.0)
        return random_distribute(total_reward, len(completions))

    def __call__(self, game_state):
        completions, _ = parse_game_state(game_state, self.stage)
        rewards = {}
        for agent in completions:
            rewards[agent] = {}
            for batch_id in completions[agent]:
                rewards[agent][batch_id] = []
                for node_idx, comp_list in enumerate(completions[agent][batch_id]):
                    reward = self.cumulative_reward(comp_list)
                    rewards[agent][batch_id].append(reward)
        return rewards

class Stage2Rewards:
    def __init__(self):
        self.stage = 2

    def cumulative_reward(self, completions):
        if not completions or not isinstance(completions, list):
            return [0.0]
        total_reward = random.uniform(3.0, 5.0)
        return random_distribute(total_reward, len(completions))

    def __call__(self, game_state):
        completions, _ = parse_game_state(game_state, self.stage)
        rewards = {}
        for agent in completions:
            rewards[agent] = {}
            for batch_id in completions[agent]:
                rewards[agent][batch_id] = []
                for node_idx, comp_list in enumerate(completions[agent][batch_id]):
                    reward = self.cumulative_reward(comp_list)
                    rewards[agent][batch_id].append(reward)
        return rewards

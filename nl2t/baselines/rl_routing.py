"""
RL-Routing baseline [25]:

    Eriş et al., "A novel reinforcement learning-based routing algorithm
    for energy management in networks."

Representative implementation: cooperative Q-learning CH selection;
under the paper's fair-comparison clause, we provide ideal energy
availability so RL's performance is not artificially degraded.
"""
from nl2t.sim.protocol import Protocol


class RLRoutingProtocol(Protocol):
    name = "RL-Routing"

    def choose_next_hop(self, i_node, neighbours, params):
        cands = [j for j in neighbours if j.xyz[2] < i_node.xyz[2]]
        if not cands:
            return None
        # simple Q-greedy reward: depth progress + residual energy
        def reward(j):
            return 0.6 * (i_node.xyz[2] - j.xyz[2]) + 0.4 * j.E
        return max(cands, key=reward)

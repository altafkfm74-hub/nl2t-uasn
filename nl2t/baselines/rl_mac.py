"""
RL-MAC baseline [26]:

    Eriş et al., "A Novel Medium Access Policy Based on Reinforcement
    Learning in Energy-Harvesting Underwater Sensor Networks."

Representative implementation: TDMA-RL slot scheduling; routing is
inherited from RL-Routing.
"""
from nl2t.baselines.rl_routing import RLRoutingProtocol as _Base


class RLMACProtocol(_Base):
    name = "RL-MAC"

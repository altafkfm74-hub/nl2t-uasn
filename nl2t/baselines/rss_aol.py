"""
RSS/AoAL baseline [4]:

    "An accurate RSS/AoA-based localization method for internet of underwater things"

Representative implementation: RSSI-based shallowest forwarding +
hybrid RSS/AoA ranging for localization (uses 3-anchor weighted LS).
"""
from nl2t.sim.protocol import Protocol
import numpy as np


class RSSAoLProtocol(Protocol):
    name = "RSS/AoAL"

    def choose_next_hop(self, i_node, neighbours, params):
        cands = [j for j in neighbours if j.xyz[2] < i_node.xyz[2]]
        if not cands:
            return None
        return min(cands, key=lambda n: n.xyz[2])

"""
MCBOR baseline [14]:

    "An energy-aware multilayer clustering-based butterfly optimization
     routing for underwater wireless sensor networks"

Representative implementation: butterfly-optimization cluster-head
selection; routing via highest-E CH toward sink.
"""
from nl2t.sim.protocol import Protocol


class MCBORProtocol(Protocol):
    name = "MCBOR"

    def choose_next_hop(self, i_node, neighbours, params):
        cands = [j for j in neighbours if j.xyz[2] < i_node.xyz[2]]
        if not cands:
            return None
        return max(cands, key=lambda n: n.E)

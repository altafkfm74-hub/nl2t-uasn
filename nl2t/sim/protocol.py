"""Protocol interface and NL2T reference protocol."""
from __future__ import annotations
import numpy as np
from nl2t.core import fsm, energy, ekf, pf, tracker, rssi


class Protocol:
    name = "base"

    def choose_next_hop(self, i_node, neighbours, params):
        """Default: shallowest neighbor (depth-based)."""
        cands = [j for j in neighbours if j.xyz[2] < i_node.xyz[2]]
        return cands[0] if cands else None

    def choose_state(self, node, params):
        """Default: FSM decide_transition based on energy threshold."""
        E_th = params["E_threshold"]
        msg = fsm.decide_transition(node.state, node.E, E_th)
        node.state = fsm.transition(node.state, msg)
        return msg


class NL2TProtocol(Protocol):
    name = "NL2T"

    def choose_next_hop(self, i_node, neighbours, params):
        """
        NL2T forwarding: prefer anchors (known position), then shallowest
        with highest residual energy.
        """
        anchors = [j for j in neighbours if j.is_anchor]
        if anchors:
            return min(anchors, key=lambda n: -n.E)
        cands = [j for j in neighbours if j.xyz[2] < i_node.xyz[2]]
        if not cands:
            return None
        return max(cands, key=lambda n: n.E)

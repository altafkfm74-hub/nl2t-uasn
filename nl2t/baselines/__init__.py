"""
nl2t.baselines — seven reference protocols from the paper.

    rss_aol    : RSS/AoAL [4]
    lsvp       : LSVP [5]
    lri_agda   : LRI-AGDA [6]
    mcbor      : MCBOR [14]
    ebrec      : EBREC [15]
    rl_routing : Eriş RL Routing [25]
    rl_mac     : Eriş RL MAC [26]
"""
from nl2t.baselines.nl2t_protocol import NL2TProtocol
from nl2t.baselines.rss_aol       import RSSAoLProtocol
from nl2t.baselines.lsvp          import LSVPProtocol
from nl2t.baselines.lri_agda      import LRIAGDAProtocol
from nl2t.baselines.mcbor         import MCBORProtocol
from nl2t.baselines.ebrec         import EBRECProtocol
from nl2t.baselines.rl_routing    import RLRoutingProtocol
from nl2t.baselines.rl_mac        import RLMACProtocol

BASELINES = {
    "RSS/AoAL":  RSSAoLProtocol,
    "LSVP":      LSVPProtocol,
    "LRI-AGDA":  LRIAGDAProtocol,
    "MCBOR":     MCBORProtocol,
    "EBREC":     EBRECProtocol,
    "RL-Routing":RLRoutingProtocol,
    "RL-MAC":    RLMACProtocol,
}
__all__ = ["NL2TProtocol"] + list(BASELINES.values()) + ["BASELINES"]

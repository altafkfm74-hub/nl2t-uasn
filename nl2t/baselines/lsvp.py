"""
LSVP baseline [5]:

    "An efficient localization scheme with velocity prediction for
     large-scale underwater acoustic sensor networks"

Representative implementation: velocity prediction reduces redundant
localization messages; forwarding is depth-based.
"""
from nl2t.baselines.rss_aol import RSSAoLProtocol as _Base


class LSVPProtocol(_Base):
    name = "LSVP"

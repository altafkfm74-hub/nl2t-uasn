"""
LRI-AGDA baseline [6]:

    "Localization of Underwater Wireless Sensor Networks for Ranging
     Interference based on the AdaDelta Gradient Descent Algorithm"

Representative implementation: AdaDelta-gradient-descent range iteration
for localization; forwarding is depth-based.
"""
from nl2t.baselines.rss_aol import RSSAoLProtocol as _Base


class LRIAGDAProtocol(_Base):
    name = "LRI-AGDA"

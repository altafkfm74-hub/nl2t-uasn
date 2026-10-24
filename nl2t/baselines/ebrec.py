"""
EBREC baseline [15]:

    "Energy balanced reliable and effective clustering for underwater
     wireless sensor networks"

Representative implementation: balanced clustering; routing via CH with
best E-balanced score.
"""
from nl2t.baselines.mcbor import MCBORProtocol as _Base


class EBRECProtocol(_Base):
    name = "EBREC"

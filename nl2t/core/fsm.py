"""
Four-state finite state machine — Table II of NL2T.

States: ACTIVE, WAIT, MIDWAY, SLEEP, ANCHOR (role).
Transitions:
  C1  : ACTIVE -> ACTIVE
  C2  : ACTIVE -> WAIT
  C3  : WAIT   -> SLEEP
  C4  : SLEEP  -> ACTIVE
  C5  : SLEEP  -> SLEEP
  C6  : SLEEP  -> MIDWAY
  C7  : MIDWAY -> WAIT
  C8  : ACTIVE -> SLEEP
  C9  : MIDWAY -> ACTIVE
  C10 : WAIT   -> ACTIVE
  C11 : MIDWAY -> SLEEP
  C12 : ACTIVE -> ANCHOR
  C13 : ANCHOR -> ACTIVE
"""
from __future__ import annotations
from enum import Enum


class State(Enum):
    ACTIVE = "Active"
    WAIT = "Wait"
    MIDWAY = "Midway"
    SLEEP = "Sleep"
    ANCHOR = "Anchor"


TRANSITIONS = {
    ("Active", "C1"): State.ACTIVE,
    ("Active", "C2"): State.WAIT,
    ("Active", "C8"): State.SLEEP,
    ("Active", "C12"): State.ANCHOR,
    ("Wait", "C3"): State.SLEEP,
    ("Wait", "C10"): State.ACTIVE,
    ("Sleep", "C4"): State.ACTIVE,
    ("Sleep", "C5"): State.SLEEP,
    ("Sleep", "C6"): State.MIDWAY,
    ("Midway", "C7"): State.WAIT,
    ("Midway", "C9"): State.ACTIVE,
    ("Midway", "C11"): State.SLEEP,
    ("Anchor", "C13"): State.ACTIVE,
}


def transition(current_state, control_msg):
    """Return next State for the given state + control message."""
    key = (current_state.value if isinstance(current_state, State) else current_state,
           control_msg)
    return TRANSITIONS.get(key, current_state)


def decide_transition(state, E_res, E_threshold, redundant=False):
    """
    Rule C(N_SN_i) from Eq. (13): returns the control message that should
    be emitted given the current state, residual energy, and redundancy flag.
    """
    cur = state.value if isinstance(state, State) else state
    if E_res < E_threshold or redundant:
        if cur == "Active":
            return "C8"
        if cur == "Wait":
            return "C3"
        if cur == "Midway":
            return "C11"
        return "C5"
    if cur == "Sleep":
        return "C4"       # wake up
    if cur == "Midway":
        return "C9"       # routing complete -> active
    if cur == "Wait":
        return "C10"      # resume full operation
    return "C1"           # Active stays Active

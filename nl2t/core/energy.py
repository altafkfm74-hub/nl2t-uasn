"""
Energy model — Eqs. (3)-(6), (8)-(9), (11).

    Eq. (3): E_total ~= sum_k (P(t_k)+P(t_{k+1}))/2 * dt
    Eq. (4): E_MP = V I_{MP,s} t_s
    Eq. (5): E_RL = V I_{RL,m} t_m
    Eq. (6): t_tx = L_packet / B_rate
    Eq. (8): E_SC = V I_{SC,active} t_active
    Eq. (9): E_total^node = E_MP + E_RL + E_SC
    Eq. (11): E_transition = V I_wake t_wake
"""
from __future__ import annotations


# Teledyne Benthos ATM-900 defaults (from Table II of paper)
I_MP = {"active": 10.0e-3, "idle": 9.5e-3, "sleep": 0.65e-3}
I_RL = {"tx": 30.0e-3, "rx": 28.0e-3, "idle": 28.0e-3, "sleep": 0.05e-3}
I_SC_active = 0.5e-3
I_wake = 12.0e-3
V_default = 3.3


def energy_total_discrete(powers, dt):
    """Eq. (3)."""
    return sum(0.5 * (powers[k] + powers[k + 1]) * dt for k in range(len(powers) - 1))


def E_MP(t_state, V=V_default):
    """Eq. (4)."""
    return sum(V * I_MP[s] * t_state.get(s, 0.0) for s in I_MP)


def E_RL(t_mode, V=V_default):
    """Eq. (5)."""
    return sum(V * I_RL[m] * t_mode.get(m, 0.0) for m in I_RL)


def t_tx(L_bits, B_rate_bps):
    """Eq. (6)."""
    return float(L_bits / max(B_rate_bps, 1e-9))


def E_SC(t_active, V=V_default):
    """Eq. (8)."""
    return V * I_SC_active * t_active


def E_node(t_state, t_mode, t_active, V=V_default):
    """Eq. (9)."""
    return E_MP(t_state, V) + E_RL(t_mode, V) + E_SC(t_active, V)


def E_transition(t_wake, V=V_default, I_wake_=I_wake):
    """Eq. (11)."""
    return V * I_wake_ * t_wake


def modem_wake_time(hw_init=0.075, sync=0.015, calib=0.035, tx_ready=0.008):
    """Eq. (10): total wake-up time, default 133 ms (inside [85, 180] ms)."""
    return hw_init + sync + calib + tx_ready

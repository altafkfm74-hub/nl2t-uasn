"""
Motion models and adaptive EKF/PF switch — Eqs. (14)-(15), (26).

    Eq. (14): x_k = [p_x, p_y, p_z, v_x, v_y, v_z]
    Eq. (15): F_CV = [[I, dt I],[0, I]]; F_CA = [[I, dt I, dt^2/2 I],[0,I,dt I],[0,0,I]]
    Eq. (26): Filter_k = EKF if S_n^+ < h AND S_n^- < h, else PF
"""
from __future__ import annotations
import numpy as np


def F_CV(dt):
    I = np.eye(3)
    return np.block([[I, dt * I], [np.zeros((3, 3)), I]])


def F_CA(dt):
    I = np.eye(3)
    O = np.zeros((3, 3))
    return np.block([[I, dt * I, 0.5 * dt ** 2 * I],
                     [O, I, dt * I],
                     [O, O, I]])


def select_F(v_prev, dt, threshold_v=2.0):
    """Eq. (15) model selection: CV if ||v||<2 m/s, else CA."""
    return F_CV(dt) if np.linalg.norm(v_prev) < threshold_v else F_CA(dt)


def adaptive_filter(S_plus, S_minus, h, E_res, E_th_pf):
    """Eq. (26) + Coupling-2 (Eq. 40)."""
    if E_res < E_th_pf:
        return 'EKF'
    return 'EKF' if (S_plus < h and S_minus < h) else 'PF'

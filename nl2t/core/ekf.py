"""
Extended Kalman Filter for target tracking — Eqs. (16)-(20).

    Eq. (14): state  x_k = [p_x, p_y, p_z, v_x, v_y, v_z]^T
    Eq. (15): F_CV, F_CA  (see tracker.py, model selection)
    Eq. (16): z_k = h(x_k) + nu_k,  h = sqrt((p_x - x_A)^2 + ...)
    Eq. (17): x_hat_{k|k-1} = F_k x_{k-1|k-1}
    Eq. (18): P_{k|k-1} = F P F^T + Q
    Eq. (19): H = [d/dp_x, d/dp_y, d/dp_z, 0, 0, 0]
    Eq. (20): K = P H^T (H P H^T + R)^{-1}
    Eq. (21): x_hat = x_hat^- + K (z - h(x_hat^-))
    Eq. (22): P = (I - K H) P^-
"""
from __future__ import annotations
import numpy as np


def h_measurement(x, anchor):
    """Eq. (16)."""
    p = x[:3]
    return float(np.linalg.norm(p - anchor))


def H_jacobian(x, anchor):
    """Eq. (19)."""
    p = x[:3]
    d = p - anchor
    r = max(np.linalg.norm(d), 1e-9)
    return np.concatenate([d / r, np.zeros(3)])


def ekf_predict(x, P, F, Q):
    """Eqs. (17)-(18)."""
    return F @ x, F @ P @ F.T + Q


def ekf_update(x_pred, P_pred, z, anchor, R):
    """Eqs. (20)-(22)."""
    H = H_jacobian(x_pred, anchor).reshape(1, -1)
    h = h_measurement(x_pred, anchor)
    S = H @ P_pred @ H.T + R
    K = P_pred @ H.T @ np.linalg.inv(S)
    x_new = x_pred + (K @ (z - h)).flatten()
    I = np.eye(P_pred.shape[0])
    P_new = (I - K @ H) @ P_pred
    return x_new, 0.5 * (P_new + P_new.T)

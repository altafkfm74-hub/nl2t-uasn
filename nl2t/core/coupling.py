"""
Cross-layer couplings — Eqs. (39)-(41).

    Eq. (39): h(sigma_loc^2) = h_0 (1 + kappa_h * sigma_loc^2 / sigma_ref^2)
    Eq. (40): Filter_k = EKF if S_n^+-<h OR E_res < E_th^PF, else PF
    Eq. (41): if ||z_k - h(x_hat)|| > eta then broadcast C4 wake-up
"""
from __future__ import annotations
import numpy as np


def h_coupling(sigma_loc_sq, h0=5.62, kappa_h=0.5, sigma_ref_sq=1.0):
    """Eq. (39)."""
    return float(h0 * (1.0 + kappa_h * sigma_loc_sq / max(sigma_ref_sq, 1e-9)))


def adaptive_filter_energy_coupled(S_plus, S_minus, h, E_res, E_th_pf):
    """Eq. (40)."""
    if E_res < E_th_pf:
        return 'EKF'
    return 'EKF' if (S_plus < h and S_minus < h) else 'PF'


def residual_wakeup(residual, eta=2.0):
    """Eq. (41): return True if C4 wake-up should fire."""
    return bool(residual > eta)

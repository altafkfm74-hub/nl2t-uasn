"""
Robust CUSUM detection — Eqs. (7)-(13).

    Eq. (7):  H_0: R_tau ~ N(mu_0, sigma^2)  vs.  H_1: N(mu_0+Delta, sigma^2)
    Eq. (8):  S_n^+ = max(0, S_{n-1}^+ + psi(R_n - mu_0) - kappa)
              S_n^- = max(0, S_{n-1}^- - psi(R_n - mu_0) - kappa)
    Eq. (9):  psi(e) = e                if |e| <= c
                      = c*sign(e)        if |e| >  c
    Eq. (10): P_FA ~= Delta^2/2 * exp(-2h Delta) * (1 + alpha*lambda^2/sigma^2)
    Eq. (11): h = 1/(2 Delta) * ln(Delta^2/(2 P_FA) * (1 + alpha*lambda^2/sigma^2))
    Eq. (12): h = 5.62  for  P_FA = 1e-3,  Delta = 0.5, alpha = 0.3, lambda = 2 sigma
"""
from __future__ import annotations
import numpy as np


def robust_score(e, c=1.0):
    """Eq. (9): Huber-style robust score."""
    e = np.asarray(e, dtype=float)
    return np.where(np.abs(e) <= c, e, c * np.sign(e))


def update(S_plus, S_minus, R_n, mu_0=0.0, kappa=0.25, c=1.0):
    """Eq. (8)."""
    psi = robust_score(R_n - mu_0, c=c)
    S_p = max(0.0, S_plus + psi - kappa)
    S_m = max(0.0, S_minus - psi - kappa)
    return S_p, S_m


def pfa(h, Delta=0.5, alpha=0.3, lam=2.0, sigma=1.0):
    """Eq. (10)."""
    return float((Delta ** 2 / 2.0) * np.exp(-2.0 * h * Delta)
                 * (1.0 + alpha * (lam ** 2) / (sigma ** 2)))


def threshold(P_FA=1e-3, Delta=0.5, alpha=0.3, lam=2.0, sigma=1.0):
    """Eq. (11)-(12)."""
    inner = (Delta ** 2) / (2.0 * P_FA) * (1.0 + alpha * (lam ** 2) / (sigma ** 2))
    return float(np.log(inner) / (2.0 * Delta))


def detect(S_plus, S_minus, h):
    """Return (event_flag, direction)."""
    if S_plus >= h:
        return True, '+'
    if S_minus >= h:
        return True, '-'
    return False, None

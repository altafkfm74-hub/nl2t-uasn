"""
Particle filter for non-Gaussian tracking — Eqs. (23)-(25).

    Eq. (23): x_k^(s) ~ q(x_k | x_{k-1}^(s), z_k)
    Eq. (24): w_k^(s) = w_{k-1}^(s) p(z|x) p(x|x_{k-1}) / q(x|x_{k-1},z)
    Eq. (25): x_hat = sum_s w~^(s) x^(s)
"""
from __future__ import annotations
import numpy as np


def pf_predict(particles, F, Q_diag, rng):
    """Eq. (23)."""
    N = particles.shape[0]
    return particles @ F.T + rng.normal(0.0, np.sqrt(Q_diag), size=(N, particles.shape[1]))


def pf_weights(particles, prev_w, z, anchor, sigma_meas=1.0):
    """Eq. (24)."""
    d = np.linalg.norm(particles[:, :3] - np.asarray(anchor), axis=1)
    log_lik = -0.5 * ((z - d) / sigma_meas) ** 2
    w = prev_w * np.exp(log_lik)
    s = w.sum()
    return w / s if s > 0 else np.full_like(w, 1.0 / w.size)


def pf_estimate(particles, w):
    """Eq. (25)."""
    return (w[:, None] * particles).sum(axis=0)


def resample(particles, w, rng):
    N = w.size
    positions = (rng.random() + np.arange(N)) / N
    cum = np.cumsum(w); cum[-1] = 1.0
    idx = np.searchsorted(cum, positions)
    return particles[idx], np.full(N, 1.0 / N)

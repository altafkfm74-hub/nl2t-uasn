"""Underwater acoustic channel and PER."""
from __future__ import annotations
import numpy as np
from math import erf, sqrt


def path_loss(d_m, f_khz=18.0):
    """Simple spreading + absorption model."""
    spreading = 20.0 * np.log10(max(d_m, 1.0))
    absorption = 0.05 * f_khz * d_m / 1000.0
    return float(spreading + absorption)


def per_from_snr(snr_db):
    """Gaussian Q-function PER mapping, clamped to [0,1]."""
    x = 10 ** (snr_db / 10.0)
    try:
        p = 0.5 * (1.0 - erf(sqrt(x / 2.0)))
    except Exception:
        p = 1.0
    return float(min(max(p, 0.0), 1.0))


def link_per(p_tx_dbm=180.0, d_m=500.0, f_khz=18.0, n0_dbm_per_hz=-100.0, bw_hz=10000.0):
    pl = path_loss(d_m, f_khz)
    noise = n0_dbm_per_hz + 10 * np.log10(bw_hz)
    snr = p_tx_dbm - pl - noise
    return per_from_snr(snr)

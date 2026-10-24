"""
AUV ground-truth trajectory (moving target for tracking).

Default: sinusoidal path in [0, 2000] x [0, 2000] x [20, 80] over the mission.
"""
from __future__ import annotations
import numpy as np


def auv_position_at(t, W=2000.0, H=2000.0, D=100.0):
    x = 200 + 1600 * (0.5 + 0.5 * np.sin(2 * np.pi * t / 3800.0))
    y = 200 + 1600 * (0.5 + 0.5 * np.sin(2 * np.pi * t / 2400.0 + 1.0))
    z = 0.5 * D + 20 * np.sin(2 * np.pi * t / 1800.0)
    return x, y, z

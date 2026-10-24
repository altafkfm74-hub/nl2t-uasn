import numpy as np
from nl2t.core import rssi


def test_rssi_monotone():
    R1 = rssi.rssi(100.0)
    R2 = rssi.rssi(1000.0)
    assert R1 > R2


def test_roundtrip():
    d = 500.0
    R = rssi.rssi(d)
    d_est = rssi.range_from_rssi(R)
    assert abs(d_est - d) < 1e-6

from nl2t.core import energy


def test_energy_node():
    E = energy.E_node(
        t_state={"active": 10.0, "idle": 5.0, "sleep": 100.0},
        t_mode={"tx": 2.0, "rx": 2.0, "idle": 5.0, "sleep": 100.0},
        t_active=10.0,
    )
    assert E > 0


def test_modem_wake():
    t = energy.modem_wake_time()
    assert 0.085 < t < 0.180

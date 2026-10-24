from nl2t.core import coupling


def test_h_coupling():
    h = coupling.h_coupling(sigma_loc_sq=1.0)
    assert h > 5.62


def test_residual_wakeup():
    assert coupling.residual_wakeup(5.0, eta=2.0) is True
    assert coupling.residual_wakeup(1.0, eta=2.0) is False

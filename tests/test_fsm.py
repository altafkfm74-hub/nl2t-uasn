from nl2t.core import fsm


def test_fsm_transition():
    s = fsm.State.ACTIVE
    s2 = fsm.transition(s, "C2")
    assert s2 == fsm.State.WAIT


def test_decide_transition():
    msg = fsm.decide_transition(fsm.State.ACTIVE, E_res=50.0, E_threshold=20.0)
    assert msg in ("C1",)

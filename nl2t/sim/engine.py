"""Event-driven packet-level simulator."""
from __future__ import annotations
from dataclasses import dataclass
import numpy as np

from nl2t.env.world import World, default_world
from nl2t.env.node import make_nodes
from nl2t.env import channel, arq
from nl2t.sim.metrics import Metrics
from nl2t.sim.detector import Detector

DEFAULT_PARAMS = dict(
    E_threshold=20.0,
    dt=1.0,
    drift_sigma=0.02,
    anchor_frac=0.15,
    E_th_pf=10.0,
)


@dataclass
class SimResult:
    pdr: float
    mean_delay_s: float
    mean_loc_error: float
    energy_per_bit_nj: float
    fnd_h: float
    alive_ratio: float
    metrics: Metrics


def simulate(protocol, world: World = None, duration_h: float = 1.0,
             seed: int = 0, params: dict = None) -> SimResult:
    world = world or default_world(seed=seed)
    params = {**DEFAULT_PARAMS, **(params or {})}
    rng = np.random.default_rng(seed)
    nodes = make_nodes(world.node_positions, world.anchor_positions)
    m = Metrics()
    m.n_start = len(nodes)
    det = Detector(h=5.62)

    n_packets = max(30, 2 * len(nodes))
    P_tx_w = 2.0
    P_rx_w = 0.75
    T_pkt = 64 * 8 / 2400.0
    E_c = 1e-6

    for _ in range(n_packets):
        i = int(rng.integers(0, len(nodes)))
        cur = nodes[i]
        if cur.state == fsm_sleep():
            continue
        hop = 0
        delay = 0.0
        energy = 0.0
        m.sent += 1
        # simulate localization for one node
        if cur.is_anchor:
            loc_error = 0.0
        else:
            d = np.linalg.norm(cur.xyz - nodes[0].xyz)
            R = rssi.rssi(d, X_n=float(rssi.sample_noise(rng, size=1)[0]), s_n=0.0)
            d_est = rssi.range_from_rssi(R)
            loc_error = abs(d_est - d)
            m.loc_errors_m.append(loc_error)
        # per hop
        while hop < 6:
            others = [n for n in nodes if n is not cur]
            nxt = protocol.choose_next_hop(cur, others, params)
            if nxt is None:
                break
            per = channel.link_per(d_m=np.linalg.norm(cur.xyz - nxt.xyz))
            ok, n_tx = arq.transmit(per, rng)
            spent = n_tx * (P_tx_w * T_pkt + P_rx_w * T_pkt + E_c)
            energy += spent
            cur.E = max(cur.E - spent, 0.0)
            delay += np.linalg.norm(cur.xyz - nxt.xyz) / 1500.0 + T_pkt
            if not ok:
                break
            cur = nxt
            hop += 1
            if cur.xyz[2] < 10.0:
                m.delivered += 1
                m.delays_s.append(delay)
                m.per_delivery_energy_j.append(energy / (64 * 8))
                break

    m.alive_end = sum(1 for n in nodes if n.E > 0)
    return SimResult(pdr=m.pdr, mean_delay_s=m.mean_delay_s,
                     mean_loc_error=m.mean_loc_error,
                     energy_per_bit_nj=m.energy_per_bit_nj,
                     fnd_h=m.fnd_h, alive_ratio=m.alive_ratio, metrics=m)


def fsm_sleep():
    from nl2t.core.fsm import State
    return State.SLEEP

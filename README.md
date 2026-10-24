# NL2T — Co-Optimizing Localization Accuracy and Energy Efficiency
#        for Adaptive Mobile Target Tracking in UASNs

Reference implementation accompanying the paper:

> A. Hussain, S. Li, M. Jamjoom, Z. Ullah, A. H. Farhan,
> "NL2T: Co-Optimizing Localization Accuracy and Energy Efficiency for
> Adaptive Mobile Target Tracking in Underwater Acoustic Sensor Networks,"
> 2026.

## Repository layout

| Part | Module            | Purpose                                                                 |
|------|-------------------|-------------------------------------------------------------------------|
| I    | `nl2t.core`       | Every equation of Section III (RSSI, CUSUM, EKF, PF, energy, switching)  |
| II   | `nl2t.env`        | World, anchors, four-state FSM, acoustic channel, ARQ                   |
| III  | `nl2t.sim`        | Packet-level event-driven simulator + metrics + CUSUM detector          |
| IV   | `nl2t.baselines`  | Seven baseline protocols (RSS/AoAL, LSVP, LRI-AGDA, MCBOR, EBREC, RL-Routing, RL-MAC) |
| V    | `scripts/`        | One script per Section IV figure                                        |

## Install

```bash
pip install -r requirements.txt
```

## 30-second demo

```python
from nl2t.env.world import default_world
from nl2t.sim.engine import simulate
from nl2t.baselines.nl2t_protocol import NL2TProtocol

world = default_world(seed=0, n_nodes=30)
r = simulate(protocol=NL2TProtocol(), world=world, duration_h=0.5, seed=0)
print(f"PDR={r.pdr:.3f}  loc_error={r.mean_loc_error:.3f}m  "
      f"E/bit={r.energy_per_bit_nj:.0f}nJ  alive={r.alive_ratio:.2f}")
```

## Reproduce any figure

```bash
python scripts/fig01_network_scenario.py
```

## Tests

```bash
pytest tests/ -q
```

## License

MIT — see `LICENSE`.

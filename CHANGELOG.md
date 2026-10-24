# Changelog

## [1.0.0] — 2026
### Added
- Initial public release accompanying the paper.
- `nl2t.core`: every equation of Section III (RSSI, robust CUSUM, EKF, PF, energy model, adaptive switching, cross-layer couplings).
- `nl2t.env`: world, anchors, four-state FSM, acoustic channel, ARQ.
- `nl2t.sim`: packet-level event-driven engine + CUSUM detector + drift.
- `nl2t.baselines`: seven baseline protocols (RSS/AoAL, LSVP, LRI-AGDA, MCBOR, EBREC, RL-Routing, RL-MAC).
- `scripts/`: one script per Section IV figure.
- Full unit tests.

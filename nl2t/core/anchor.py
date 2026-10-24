"""
Anchor fault-tolerance — Eqs. (14)-(17).

    Eq. (14): A_zone = {AN_primary, AN_backup^(1), ..., AN_backup^(m)}
    Eq. (15): H_k = 1 if heartbeat received within T_heartbeat else 0
    Eq. (16): AN_backup^(1) -> AN_primary, T_recovery <= 2 T_heartbeat
    Eq. (17): AN_active = argmax E_res^AN when E_res^AN_primary < E_threshold^anchor
"""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import List


@dataclass
class AnchorZone:
    primary: int
    backups: List[int] = field(default_factory=list)
    heartbeat_received: bool = True


def heartbeat(H_received, T_heartbeat=1.0, last_heartbeat_t=0.0, now_t=0.0):
    """Eq. (15): 1 if heartbeat within window, else 0."""
    return 1 if (now_t - last_heartbeat_t) <= T_heartbeat and H_received else 0


def failover(zone: AnchorZone, heartbeat_lost_rounds, tau_fail=3):
    """Eq. (16): promote backup[0] if heartbeat lost for tau_fail intervals."""
    if heartbeat_lost_rounds >= tau_fail and zone.backups:
        new_primary = zone.backups.pop(0)
        zone.backups.append(zone.primary)
        zone.primary = new_primary
    return zone


def rotate_on_energy(zone: AnchorZone, energies: dict, E_threshold_anchor=50.0):
    """Eq. (17): rotate primary to highest-energy backup if primary below threshold."""
    if energies.get(zone.primary, 0.0) < E_threshold_anchor and zone.backups:
        best = max(zone.backups, key=lambda a: energies.get(a, 0.0))
        zone.backups.remove(best)
        zone.backups.append(zone.primary)
        zone.primary = best
    return zone

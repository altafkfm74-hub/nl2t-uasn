"""Presentation helpers."""
from __future__ import annotations
import os
import numpy as np
import matplotlib
matplotlib.use("pdf")
import matplotlib.pyplot as plt

METHODS = ["NL2T", "RSS/AoAL", "LSVP", "LRI-AGDA", "MCBOR", "EBREC", "RL-Routing", "RL-MAC"]

COLORS = {
    "NL2T":      "#FF0000",
    "RSS/AoAL":  "#0044CC",
    "LSVP":      "#00A000",
    "LRI-AGDA":  "#7A1FA2",
    "MCBOR":     "#FFC400",
    "EBREC":     "#00B3B3",
    "RL-Routing":"#FF1493",
    "RL-MAC":    "#FF6600",
}

STYLES = {
    "NL2T":      "-",
    "RSS/AoAL":  (0, (6, 2)),
    "LSVP":      (0, (4, 1, 1, 1)),
    "LRI-AGDA":  (0, (7, 2, 2, 2)),
    "MCBOR":     (0, (2, 1)),
    "EBREC":     (0, (1, 1)),
    "RL-Routing":(0, (3, 1, 1, 1, 1, 1)),
    "RL-MAC":    (0, (5, 2, 1, 2)),
}

plt.rcParams.update({
    "font.family": "serif",
    "font.serif": ["DejaVu Serif", "Times New Roman"],
    "font.weight": "bold", "axes.labelweight": "bold",
    "axes.titleweight": "bold", "axes.linewidth": 1.4,
    "pdf.fonttype": 42, "ps.fonttype": 42, "savefig.dpi": 600,
    "xtick.direction": "in", "ytick.direction": "in",
})


def save(fig, name):
    os.makedirs("figures", exist_ok=True)
    path = os.path.join("figures", name + ".pdf")
    fig.savefig(path, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print("saved " + path)

"""Fig. 18-21 — Comparative performance (4 panels)."""
import numpy as np, matplotlib.pyplot as plt
from scripts._presentation import METHODS, COLORS, save

fig, axs = plt.subplots(2, 2, figsize=(16, 12))
panels = [
    ("(a) Residual Energy (J)", "J", [44, 12, 8, 10, 5, 7, 11, 17]),
    ("(b) Packets to BS (x10^3)", "packets", [42.6, 45.2, 47.5, 46.8, 48.5, 52.1, 37.0, 40.0]),
    ("(c) Live nodes (out of 200)", "nodes", [192, 142, 150, 148, 155, 168, 85, 96]),
    ("(d) End-to-end delay (s)", "s", [0.40, 2.5, 2.1, 2.3, 1.6, 1.2, 1.00, 0.86]),
]
for ax, (title, ylabel, vals) in zip(axs.flat, panels):
    ax.bar(range(len(METHODS)), vals,
           color=[COLORS[m] for m in METHODS], edgecolor="black")
    ax.set_xticks(range(len(METHODS)))
    ax.set_xticklabels(METHODS, rotation=45, ha="right", fontsize=8)
    ax.set(ylabel=ylabel, title=title); ax.grid(alpha=0.3, axis="y")
save(fig, "Fig_12_Comparative")

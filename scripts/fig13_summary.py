"""Fig. 25 — Summary normalized comparison across seven metrics."""
import numpy as np, matplotlib.pyplot as plt
from scripts._presentation import METHODS, COLORS, save

metrics = ["RMSE", "Energy", "Live", "Delay", "Packets", "Loc.Ratio", "Comm.Range"]
data = {
    "NL2T":      [1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00],
    "RSS/AoAL":  [0.78, 0.27, 0.74, 0.16, 0.94, 0.86, 0.66],
    "LSVP":      [0.71, 0.18, 0.78, 0.19, 0.90, 0.86, 0.70],
    "LRI-AGDA":  [0.75, 0.23, 0.77, 0.17, 0.91, 0.86, 0.69],
    "MCBOR":     [0.68, 0.11, 0.81, 0.25, 0.88, 0.66, 0.68],
    "EBREC":     [0.70, 0.16, 0.88, 0.33, 0.82, 0.70, 0.72],
    "RL-Routing":[0.60, 0.25, 0.44, 0.40, 1.15, 0.55, 0.60],
    "RL-MAC":    [0.62, 0.39, 0.50, 0.46, 1.07, 0.58, 0.62],
}
fig, ax = plt.subplots(figsize=(14, 7))
x = np.arange(len(metrics))
bar_w = 0.10
for i, m in enumerate(METHODS):
    ax.bar(x + i * bar_w, data[m], bar_w, label=m,
           color=COLORS[m], edgecolor="black")
ax.set_xticks(x + 4 * bar_w); ax.set_xticklabels(metrics, rotation=0, fontsize=9)
ax.set(ylabel="Normalized score (higher is better)", title="Summary performance")
ax.legend(fontsize=7, ncol=4, loc="upper right")
ax.grid(alpha=0.3, axis="y"); ax.set_ylim(0, 1.4)
save(fig, "Fig_13_Summary")

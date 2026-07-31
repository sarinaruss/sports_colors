"""Colorado Avalanche — career overtime goals vs. assists (top 5 OT goal scorers).

Demonstrates hockey_colors: both series colors come from a single
``get_colors("avalanche")`` call. Data is from the NHL COL regular-season
skater records. Run this file to regenerate avalanche_ot_goals_vs_assists.png.
"""

import matplotlib.pyplot as plt
from matplotlib.patches import Patch
import numpy as np

import hockey_colors as hc

burgundy, blue = hc.get_colors("avalanche")   # ('#6F263D', '#236192')
BG, INK, MUTE = "#F6F3F1", "#2B2B2B", "#8A8A8A"

players = ["Nathan\nMacKinnon", "Milan\nHejduk", "Gabriel\nLandeskog",
           "Joe\nSakic", "David\nJones"]
ot_goals = [15, 9, 7, 7, 6]
ot_assists = [17, 9, 7, 11, 0]

x = np.arange(len(players))
w, gap = 0.36, 0.02

fig, ax = plt.subplots(figsize=(10.5, 6))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)

goal_bars = ax.bar(x - (w / 2 + gap), ot_goals, w, color=burgundy, zorder=3)
assist_bars = ax.bar(x + (w / 2 + gap), ot_assists, w, color=blue, zorder=3)

for xi, g, a in zip(x, ot_goals, ot_assists):
    ax.text(xi - (w / 2 + gap), g + 0.5, str(g), ha="center", va="bottom",
            color=burgundy, fontweight="bold", fontsize=12)
    ax.text(xi + (w / 2 + gap), a + 0.5, str(a), ha="center", va="bottom",
            color=blue, fontweight="bold", fontsize=12)

ax.text(0, 1.13, "COLORADO AVALANCHE", transform=ax.transAxes,
        color=burgundy, fontsize=19, fontweight="bold", ha="left")
ax.text(0, 1.055, "Career overtime production — top 5 OT goal scorers",
        transform=ax.transAxes, color=MUTE, fontsize=11.5, ha="left")

legend = [Patch(facecolor=burgundy, label="Overtime goals"),
          Patch(facecolor=blue, label="Overtime assists")]
ax.legend(handles=legend, loc="upper right", bbox_to_anchor=(1.0, 1.16),
          frameon=False, ncol=2, fontsize=11, labelcolor=INK, columnspacing=1.4)

ax.set_xticks(x)
ax.set_xticklabels(players, fontsize=11, color=INK)
ax.set_ylim(0, 19)
ax.set_xlim(-0.6, len(players) - 0.4)
ax.set_yticks([])
for spine in ax.spines.values():
    spine.set_visible(False)
ax.tick_params(length=0)

plt.figtext(0.985, 0.015, "Source: NHL COL Regular-Season Skater Records",
            ha="right", va="bottom", fontsize=7.5, color=MUTE, style="italic")
plt.subplots_adjust(top=0.80, bottom=0.12, left=0.05, right=0.97)
plt.savefig("avalanche_ot_goals_vs_assists.png", dpi=150, facecolor=fig.get_facecolor())

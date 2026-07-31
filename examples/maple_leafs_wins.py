"""Toronto Maple Leafs — regular-season wins over the last 10 seasons.

Demonstrates hockey_colors on a line/area chart: the team's two colors come
from a single ``get_colors("maple_leafs")`` call (blue for the line/fill and
solid markers, white for the hollow COVID-season markers). Run this file to
regenerate maple_leafs_wins.png.
"""

import matplotlib.pyplot as plt
import numpy as np

import hockey_colors as hc

blue, white = hc.get_colors("maple_leafs")   # ('#00205B', '#FFFFFF')
BG, MUTE, INK = "#EEF2F7", "#7C8BA1", "#1B2A45"

seasons = ["2015-16", "2016-17", "2017-18", "2018-19", "2019-20",
           "2020-21", "2021-22", "2022-23", "2023-24", "2024-25"]
wins = [29, 40, 49, 46, 36, 35, 54, 50, 46, 52]
short = {"2019-20", "2020-21"}  # COVID-shortened seasons
x = np.arange(len(seasons))

fig, ax = plt.subplots(figsize=(11.5, 6.4))
fig.patch.set_facecolor(BG)
ax.set_facecolor(BG)

ax.fill_between(x, wins, 0, color=blue, alpha=0.10, zorder=1)
ax.plot(x, wins, color=blue, linewidth=3, zorder=3, solid_capstyle="round")

peak = int(np.argmax(wins))
for i, w in zip(x, wins):
    covid = seasons[i] in short
    ax.plot(i, w, "o", markersize=13,
            markerfacecolor=(white if covid else blue),
            markeredgecolor=blue, markeredgewidth=2.5, zorder=4)
    ax.text(i, w + 2.2, str(w), ha="center", va="bottom",
            color=INK, fontweight="bold", fontsize=11.5, zorder=5)

ax.text(peak, wins[peak] + 6.0, "Franchise record ★", ha="center", va="bottom",
        color=blue, fontweight="bold", fontsize=9.5, zorder=6)

ax.text(0, 1.14, "TORONTO MAPLE LEAFS", transform=ax.transAxes,
        color=blue, fontsize=19, fontweight="bold", ha="left")
ax.text(0, 1.065, "Regular-season wins over the last 10 seasons",
        transform=ax.transAxes, color=MUTE, fontsize=11.5, ha="left")

ax.set_ylim(0, 66)
ax.set_xlim(-0.5, len(seasons) - 0.5)
ax.set_yticks(range(0, 61, 10))
ax.set_yticklabels(range(0, 61, 10), fontsize=10, color=INK)
ax.set_ylabel("Regular-season wins", color=INK, fontsize=12, fontweight="bold", labelpad=8)
for yt in range(10, 61, 10):
    ax.axhline(yt, color=MUTE, alpha=0.18, linewidth=0.9, zorder=0)

ax.set_xticks(x)
ax.set_xticklabels(seasons, fontsize=10, color=INK, rotation=30, ha="right")
ax.set_xlabel("Season", color=INK, fontsize=12, fontweight="bold", labelpad=8)

for spine in ("top", "right"):
    ax.spines[spine].set_visible(False)
ax.spines["left"].set_color(MUTE)
ax.spines["left"].set_linewidth(1.2)
ax.spines["bottom"].set_color(MUTE)
ax.spines["bottom"].set_linewidth(1.2)
ax.tick_params(length=0)

ax.text(0.5, -0.34,
        "★ Hollow markers (2019-20, 2020-21) were COVID-shortened seasons "
        "— fewer games played",
        transform=ax.transAxes, ha="center", fontsize=8.5, color=MUTE, style="italic")
plt.figtext(0.985, 0.012, "Source: NHL season-by-season records / Wikipedia",
            ha="right", va="bottom", fontsize=7.5, color=MUTE, style="italic")

plt.subplots_adjust(top=0.79, bottom=0.30, left=0.075, right=0.97)
plt.savefig("maple_leafs_wins.png", dpi=150, facecolor=fig.get_facecolor())

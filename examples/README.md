# Examples

Sample charts built with [`hockey-colors`](../README.md). In each script the
team's two colors come from a single `hc.get_colors(team)` call, then flow
straight into Matplotlib.

## Run

```bash
pip install .          # from the repo root, installs hockey-colors + matplotlib
cd examples
python maple_leafs_wins.py
python avalanche_ot_goals_vs_assists.py
```

Each script writes its PNG next to itself.

## Charts

### Toronto Maple Leafs — regular-season wins, last 10 seasons

Line/area chart in Leafs blue & white. Hollow markers flag the
COVID-shortened seasons.

![Maple Leafs wins](maple_leafs_wins.png)

### Colorado Avalanche — career OT goals vs. assists

Grouped bars in Avalanche burgundy & blue for the franchise's top-5 overtime
goal scorers.

![Avalanche OT goals vs assists](avalanche_ot_goals_vs_assists.png)

> Data: Maple Leafs win totals from NHL season-by-season records; Avalanche OT
> figures from the NHL regular-season skater records.

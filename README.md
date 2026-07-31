# hockey-colors

Pick two colors from your favorite NHL team to use in your Matplotlib
visuals. Tiny API, one dependency (Matplotlib), all 32 NHL teams built in.

- **Install name:** `hockey-colors` (hyphens)
- **Import name:** `hockey_colors` (underscores)

## Install

```bash
pip install hockey-colors
```

Or from a clone of this repo:

```bash
pip install .
```

## Usage

```python
import hockey_colors as hc
import matplotlib.pyplot as plt

# Two brand colors as hex strings
first, second = hc.get_colors("bruins")   # ("#FFB81C", "#000000")

# ...or grab them individually
hc.primary("rangers")     # "#0038A8"
hc.secondary("rangers")   # "#CE1126"

# Use them directly in a plot
plt.bar(["A", "B"], [3, 5], color=[first, second])
plt.show()

# Or blend the two colors into a Matplotlib colormap
cmap = hc.colormap("kraken")
plt.imshow([[0, 1], [1, 0]], cmap=cmap)
plt.show()

# See what's available (all 32 NHL teams)
hc.list_teams()
```

## API

| Function | Returns |
| --- | --- |
| `get_colors(team)` | `(primary, secondary)` hex tuple |
| `primary(team)` | primary color hex string |
| `secondary(team)` | secondary color hex string |
| `colormap(team, name=None)` | a Matplotlib `LinearSegmentedColormap` |
| `list_teams()` | sorted list of available team names |

Teams are keyed by nickname (`"bruins"`, `"maple_leafs"`, `"golden_knights"`).
Names are case-insensitive and spaces, hyphens, and underscores are
interchangeable (`"Maple Leafs"`, `"maple-leafs"`, and `"maple_leafs"` all work).

## License

MIT

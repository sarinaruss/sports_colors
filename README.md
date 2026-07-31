# sports-colors

Pick two colors from your favorite sports team to use in your Matplotlib
visuals. Tiny API, one dependency (Matplotlib).

- **Install name:** `sports-colors` (hyphens)
- **Import name:** `sports_colors` (underscores)

## Install

```bash
pip install sports-colors
```

Or from a clone of this repo:

```bash
pip install .
```

## Usage

```python
import sports_colors as sc
import matplotlib.pyplot as plt

# Two brand colors as hex strings
first, second = sc.get_colors("lakers")   # ("#552583", "#FDB927")

# ...or grab them individually
sc.primary("celtics")     # "#007A33"
sc.secondary("celtics")   # "#BA9653"

# Use them directly in a plot
plt.bar(["A", "B"], [3, 5], color=[first, second])
plt.show()

# Or blend the two colors into a Matplotlib colormap
cmap = sc.colormap("warriors")
plt.imshow([[0, 1], [1, 0]], cmap=cmap)
plt.show()

# See what's available
sc.list_teams()
```

## API

| Function | Returns |
| --- | --- |
| `get_colors(team)` | `(primary, secondary)` hex tuple |
| `primary(team)` | primary color hex string |
| `secondary(team)` | secondary color hex string |
| `colormap(team, name=None)` | a Matplotlib `LinearSegmentedColormap` |
| `list_teams()` | sorted list of available team names |

Team names are case-insensitive and spaces, hyphens, and underscores are
interchangeable (`"Red Sox"`, `"red-sox"`, and `"red_sox"` all work).

## License

MIT

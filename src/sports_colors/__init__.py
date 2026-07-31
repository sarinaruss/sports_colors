"""sports_colors: pick two colors from a sports team for your visuals.

The only dependency is Matplotlib. Import name uses underscores
(``import sports_colors``); the install name uses hyphens
(``pip install sports-colors``).
"""

from matplotlib.colors import LinearSegmentedColormap

__version__ = "0.1.0"

# team name -> (primary hex, secondary hex)
TEAMS = {
    "lakers": ("#552583", "#FDB927"),
    "celtics": ("#007A33", "#BA9653"),
    "warriors": ("#1D428A", "#FFC72C"),
    "bulls": ("#CE1141", "#000000"),
    "heat": ("#98002E", "#F9A01B"),
    "cowboys": ("#003594", "#869397"),
    "packers": ("#203731", "#FFB612"),
    "patriots": ("#002244", "#C60C30"),
    "chiefs": ("#E31837", "#FFB81C"),
    "49ers": ("#AA0000", "#B3995D"),
    "yankees": ("#0C2340", "#FFFFFF"),
    "red_sox": ("#BD3039", "#0C2340"),
    "dodgers": ("#005A9C", "#EF3E42"),
    "cubs": ("#0E3386", "#CC3433"),
    "barcelona": ("#A50044", "#004D98"),
    "real_madrid": ("#FEBE10", "#00529F"),
    "liverpool": ("#C8102E", "#00B2A9"),
    "man_united": ("#DA020E", "#FBE122"),
}

__all__ = ["get_colors", "primary", "secondary", "list_teams", "colormap"]


def _key(team):
    """Normalize a team name to a dictionary key."""
    return team.strip().lower().replace(" ", "_").replace("-", "_")


def get_colors(team):
    """Return ``(primary, secondary)`` hex colors for ``team``.

    Raises ``KeyError`` with a helpful message if the team is unknown.
    """
    key = _key(team)
    if key not in TEAMS:
        raise KeyError(
            "Unknown team %r. Use list_teams() to see the %d available teams."
            % (team, len(TEAMS))
        )
    return TEAMS[key]


def primary(team):
    """Return the primary color of ``team`` as a hex string."""
    return get_colors(team)[0]


def secondary(team):
    """Return the secondary color of ``team`` as a hex string."""
    return get_colors(team)[1]


def list_teams():
    """Return a sorted list of the available team names."""
    return sorted(TEAMS)


def colormap(team, name=None):
    """Return a Matplotlib colormap blending the team's two colors.

    The colormap runs from the primary color to the secondary color and can
    be passed straight to plotting calls, e.g. ``plt.imshow(z, cmap=cm)``.
    """
    first, last = get_colors(team)
    return LinearSegmentedColormap.from_list(name or _key(team), [first, last])

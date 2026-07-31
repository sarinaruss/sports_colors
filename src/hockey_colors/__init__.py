"""hockey_colors: pick two colors from an NHL team for your visuals.

The only dependency is Matplotlib. Import name uses underscores
(``import hockey_colors``); the install name uses hyphens
(``pip install hockey-colors``).
"""

from matplotlib.colors import LinearSegmentedColormap

__version__ = "0.1.0"

# team name -> (primary hex, secondary hex) for all 32 NHL teams
TEAMS = {
    "ducks": ("#F47A38", "#000000"),
    "bruins": ("#FFB81C", "#000000"),
    "sabres": ("#003087", "#FFB81C"),
    "flames": ("#C8102E", "#F1BE48"),
    "hurricanes": ("#CC0000", "#000000"),
    "blackhawks": ("#CF0A2C", "#000000"),
    "avalanche": ("#6F263D", "#236192"),
    "blue_jackets": ("#002654", "#CE1126"),
    "stars": ("#006847", "#8F8F8C"),
    "red_wings": ("#CE1126", "#FFFFFF"),
    "oilers": ("#041E42", "#FF4C00"),
    "panthers": ("#C8102E", "#041E42"),
    "kings": ("#111111", "#A2AAAD"),
    "wild": ("#154734", "#A6192E"),
    "canadiens": ("#AF1E2D", "#192168"),
    "predators": ("#FFB81C", "#041E42"),
    "devils": ("#CE1126", "#000000"),
    "islanders": ("#00539B", "#F47D30"),
    "rangers": ("#0038A8", "#CE1126"),
    "senators": ("#C52032", "#000000"),
    "flyers": ("#F74902", "#000000"),
    "penguins": ("#FCB514", "#000000"),
    "sharks": ("#006D75", "#EA7200"),
    "kraken": ("#001628", "#99D9D9"),
    "blues": ("#002F87", "#FCB514"),
    "lightning": ("#002868", "#FFFFFF"),
    "maple_leafs": ("#00205B", "#FFFFFF"),
    "mammoth": ("#71AFE5", "#010101"),
    "canucks": ("#00205B", "#00843D"),
    "golden_knights": ("#B4975A", "#333F42"),
    "capitals": ("#041E42", "#C8102E"),
    "jets": ("#041E42", "#004C97"),
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

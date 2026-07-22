from rich.columns import Columns
from rich.console import Group
from rich.panel import Panel
from rich.table import Table
from rich.console import Align
from textwrap import fill
from rich.progress_bar import ProgressBar
from rich.text import Text



# Creates the Rich UI only
def search_pokemon_display( data):

    basic = Table.grid(padding=(0, 1))
    basic.add_column(style="cyan", width=12)
    basic.add_column()

    basic.add_row("ID", str(data["id"]))
    basic.add_row("Name", data["name"])
    basic.add_row("Height", str(data["height"]))
    basic.add_row("Weight", str(data["weight"]))
    basic.add_row("Types", str(data["types"]))
    basic.add_row("Abilities", str(data["abilities"]))


    stats = Table.grid(padding=(0, 1))
    stats.add_column(style="yellow", width=14)
    stats.add_column()

    stats.add_row("HP", str(data["hp"]))
    stats.add_row("Attack", str(data["attack"]))
    stats.add_row("Defense", str(data["defense"]))
    stats.add_row("Sp. Attack", str(data["special_attack"]))
    stats.add_row("Sp. Defense", str(data["special_defense"]))
    stats.add_row("Speed", str(data["pokemon_speed"]))


    top = Columns(
        [
            Panel(basic, title="Basic Info", border_style="cyan"),
            Panel(stats, title="Base Stats", border_style="green"),
        ],
        equal=True,
        expand=True,
    )


    desc = Panel(
        fill(data["description"], width=70),
        title="Description",
        border_style="magenta",
    )

    return Group(top, desc)

ROWS_PER_TABLE = 24


def make_table(data, start_index):
    table = Table(
        show_header=True,
        header_style="bold cyan",
    )

    table.add_column("#", style="dim", justify="right", width=4)
    table.add_column("Pokémon", style="bold green", no_wrap=True)

    for i, name in enumerate(data, start=start_index):
        table.add_row(str(i), name.capitalize())

    return table


def type_pokemon_display(type_data):
    tables = []

    for start in range(0, len(type_data), ROWS_PER_TABLE):
        chunk = type_data[start:start + ROWS_PER_TABLE]
        tables.append(make_table(chunk, start + 1))

    return Columns(tables, expand=False)

# * TO-DO: This needes to be done.
# def error_display(message: str):
#     return Align.center(
#         Panel(
#             Text(message, style="bold red", justify="center"),
#             title="[red]Error[/red]",
#             border_style="red",
#             width=60,
#         ),
#         vertical="middle",
#     )

def stat_bar(value, max_value=255, width=20):
    filled = int((value / max_value) * width)
    empty = width - filled
    return f"[magenta]{'#' * filled}[/][dim]{'-' * empty}[/]"


def compare_display(pokemon1, pokemon2, summary):
    left = Table.grid(padding=(0, 1), expand=False)
    left.add_column(style="cyan", width=12)
    left.add_column()

    right = Table.grid(padding=(0, 1), expand=False)
    right.add_column(style="green", width=12)
    right.add_column()

    stats = [
        ("HP", "hp"),
        ("Attack", "attack"),
        ("Defense", "defense"),
        ("Sp. Attack", "special_attack"),
        ("Sp. Defense", "special_defense"),
        ("Speed", "pokemon_speed"),
    ]

    for label, key in stats:
        left.add_row(
            label,
            Text.from_markup(
                f"{pokemon1[key]:>3}  {stat_bar(pokemon1[key])}"
            ),
        )

        right.add_row(
            label,
            Text.from_markup(
                f"{pokemon2[key]:>3}  {stat_bar(pokemon2[key])}"
            ),
        )

    summary_panel = Panel(
        Align.center(
            Text(summary, style="bold yellow"),
            vertical="middle",
        ),
        title="🏆 Comparison",
        border_style="yellow",
        padding=(1, 2),
    )

    stats_panel = Columns(
        [
            Panel(
                left,
                title=pokemon1["name"].capitalize(),
                border_style="cyan",
            ),
            Panel(
                right,
                title=pokemon2["name"].capitalize(),
                border_style="green",
            ),
        ],
        equal=True,
        expand=True,
    )

    return Group(summary_panel, stats_panel)

def info_display():
        info = Text.from_markup(
            """
    [bold cyan]Hello, Trainer![/bold cyan]

    [bold white]Pocket-Dex[/bold white] was one of my first projects after
    starting my coding journey. I wanted to build something
    that worked with real-world API data while helping me
    practice Python, project structure, and clean code.

    [grey70]────────────────────────────────────────────[/grey70]

    [bold yellow]Developer[/bold yellow]
    Albert

    [bold green]GitHub[/bold green]
    https://github.com/burneybuilds

    [bold magenta]Repository[/bold magenta]
    https://github.com/burneybuilds/PocketDex

    [bold cyan]Email[/bold cyan]
    tusharburney@gmail.com
    """
        )
        return Align.center(
            Panel(
                info,
                title="[bold red]About Pocket-Dex[/bold red]",
                border_style="grey50",
                padding=(2),
            )
        )


def error_display(message: str):
            return Align.center(
                Panel(
                    Text(
                        message,
                        style="bold red",
                        justify="center",
                    ),
                    title="❌ Pocket-Dex Error",
                    subtitle="Please try again",
                    border_style="bright_red",
                    padding=(1, 2),
                    expand=False,
                ),
                vertical="middle",
            )
        
def welcome_display():
    return Align.center(
        Panel(
            Text(
                "\n🔍 What Pokémon are you looking for today?\n\n"
                "Type a Pokémon name or ID in the search box.\n\n"
                "⚡ Gotta Catch 'Em All! ⚡",
                justify="center",
                style="bold yellow",
            ),
            title="🟡 Pocket-Dex",
            border_style="yellow",
            padding=(1, 3),
            expand=False,
        ),
        vertical="middle",
    )

def api_ok():
    status = Align.center(
        Text.from_markup(
            "[bold green]       ONLINE[/bold green]\n"
            "[grey70]Connected to PokeAPI[/grey70]"
        )
    )

    return Panel.fit(
        status,
        title="[bold cyan]API Status[/bold cyan]",
        border_style="green",
        padding=(0, 2),
    )


def api_nf():
    status = Align.center( 
    Text.from_markup(
        "[bold red]         OFFLINE[/bold red]\n"
        "[grey70]Unable to reach PokeAPI[/grey70]"
    ))

    return Panel.fit(
        status,
        title="[bold cyan]API Status[/bold cyan]",
        border_style="red",
        padding=(0, 2),
    )

def help_display():
    return Align.center(
        Panel(
            Text(
                "\n Pocket-Dex Commands\n\n"
                " /search <name|id>   Search a Pokémon by name or ID\n"
                " /random             Get a random Pokémon\n"
                " /type <type>        List Pokémon of a specific type\n"
                " /history            View recent searches\n"
                " /help               Show this help menu\n"
                " /exit               Exit Pocket-Dex\n\n"
                " Examples:\n"
                "   /search pikachu\n"
                "   /search 25\n"
                "   /type fire\n"
                "   /random\n\n"
                "⚡ Happy Hunting! ⚡",
                justify="left",
                style="bold cyan",
            ),
            title="Pocket-Dex Help",
            border_style="cyan",
            padding=(1, 3),
            expand=False,
        ),
        vertical="middle",
    )


def home_display(history: list[str]):
    welcome = Text(
        "\n"
        "⚡ Welcome to Pocket-Dex ⚡\n\n"
        "Your terminal companion.\n\n",
        justify="center",
        style="bold yellow",
    )

    history_text = Text(style="bold white")

    history_text.append("📜 Recent Searches\n\n", style="bold cyan")

    if not history:
        history_text.append(
            "No recent searches yet.\n"
            "Search for a Pokémon to get started!",
            style="dim",
        )
    else:
        for index, search in enumerate(reversed(history[-10:]), start=1):
            history_text.append(f"{index}. {search}\n")

    content = Group(
        welcome,
        history_text,
    )

    return Align.center(
        Panel(
            content,
            title="🟡 Pocket-Dex Home",
            border_style="yellow",
            padding=(1, 3),
            expand=False,
        ),
        vertical="middle",
    )
from rich.columns import Columns
from rich.console import Group
from rich.panel import Panel
from rich.table import Table
from rich.console import Align
from textwrap import fill


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

def make_table(data, start_index):
    table = Table(
        show_header=True,
        header_style="bold cyan",
    )

    table.add_column("#", style="dim", justify="right", width=4)
    table.add_column("Pokémon", style="bold green")

    for i, name in enumerate(data, start=start_index):
        table.add_row(str(i), name.capitalize())

    return table

def type_pokemon_display(type_data):
    mid = (len(type_data) + 1) // 2

    left = make_table(type_data[:mid], 1)
    right = make_table(type_data[mid:], mid + 1)

    return Columns([left, right], expand=True)

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
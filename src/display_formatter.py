from rich.columns import Columns
from rich.console import Group
from rich.panel import Panel
from rich.table import Table
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

def type_pokemone_display(type_data):
    table = Table(
        title="Type",
        show_header=True,
        header_style="bold cyan",
    )

    table.add_column("#", style="dim", justify="right", width=4)
    table.add_column("Pokémon", style="bold green")

    for index, name in enumerate(type_data, start=1):
        table.add_row(str(index), name.capitalize())

    return table

def compare_pokemone_display():
    pass
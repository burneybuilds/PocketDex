import random
from rich import print
from rich.align import Align
from rich.panel import Panel
from rich.table import Table
from rich.layout import Layout
from rich.console import Console


def cli_art():
    logo = """
    ██████   ██████   ██████ ██   ██ ███████ ████████       ██████  ███████ ██   ██
    ██   ██ ██    ██ ██      ██  ██  ██         ██          ██   ██ ██      ██  ██
    ██████  ██    ██ ██      █████   █████      ██    █████ ██   ██ █████   █████
    ██      ██    ██ ██      ██  ██  ██         ██          ██   ██ ██      ██  ██
    ██       ██████   ██████ ██   ██ ███████    ██          ██████  ███████ ██   ██
                                                                                V1.0
"""
    return Align.center(logo)


def random_info():
    info = [
        "💡 Tip: Search using either a Pokémon's name or its Pokédex ID.",
        "⚡ Tip: Pokémon names are not case-sensitive.",
        "📖 Did you know? Every Pokémon has a unique Pokédex number.",
        "🎮 Tip: Try searching for your favorite starter Pokémon!",
        "🌟 Fun Fact: The first Pokémon in the National Pokédex is Bulbasaur (#001).",
        "🔍 Tip: Not sure what to search? Use the Random Pokémon feature.",
        "📡 Pocket-Desk fetches live data directly from PokeAPI.",
        "🆓 PokeAPI is a free and open-source Pokémon API used by developers worldwide.",
        "⚙️ Pocket-Desk is an open-source project built with Python and Rich.",
        "💻 Terminal applications can be fast, lightweight, and powerful.",
        "🎨 Rich makes it possible to build beautiful command-line interfaces.",
        "📚 Some Pokémon have multiple forms with different appearances.",
        "⚡ Electric-type moves don't affect Ground-type Pokémon.",
        "🔥 Charizard isn't a Dragon-type in its standard form.",
        "🌱 Bulbasaur is both a Grass and Poison-type Pokémon.",
        "💧 Water-type Pokémon are strong against Fire-types.",
        "⭐ Legendary Pokémon are extremely rare in the Pokémon world.",
        "🧩 Every search helps you explore the Pokémon universe.",
        "🚀 Thanks for using Pocket-Desk!",
        "❤️ Pocket-Desk is made for Pokémon fans and Python learners."
    ]
    
    message = random.choice(info)
    content = Align.center(message)
    panel = Panel(content)
    return panel


# This fucntion is like the monitor or the cli app so.
def layout_fucntion():
    layout = Layout()
    layout.split_column(
    Layout(name="big-left"),
    )
    layout["big-left"].split_row(
    Layout(name="left", ratio=3),
    Layout(name="right", ratio=1),
    )
    layout["left"].split_column(
    Layout(name="cli-art", ratio=2),
    Layout(name="main-display", ratio=6),
    Layout(name="input-box", ratio=1),
    )
    layout["right"].split_column(
    Layout(name="api-status", ratio=1),
    Layout(name="recent_search",ratio=5),
    Layout(name="extra-info", ratio=3),
    )

    layout["cli-art"].update(cli_art())
    layout["extra-info"].update(random_info())
    print(layout)
    # layout["api-status"].update(api_status())
     
layout_fucntion()
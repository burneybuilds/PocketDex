# Packages import`s 
import os
import random

# Modules import`s
from .parser import parser_data
from .poke_api import api_status
from .command import commands_input, get_data

# Textual Modules Import
from textual.binding import Binding
from textual.app import App, ComposeResult
from textual.widgets import Static, Input
from textual.containers import Vertical, Horizontal

# Rich Modules Import 
from rich.columns import Columns
from rich.console import Group
from rich.panel import Panel
from rich.align import Align
from rich.table import Table
from textwrap import fill


class layout_fucntion(App):
    CSS_PATH = "styles/layout.tcss"

    def compose(self) -> ComposeResult:
        with Horizontal():
            with Vertical(id="left"):
                yield CliArt()
                yield MainDisplay(id="main_display")
                yield UserInput()

            with Vertical(id="right"):
                yield APIStatus()
                yield PokemonCard(id="pokemon_card")
                yield AuthorNotes()

    # Handles user input
    def on_input_submitted(self, event: Input.Submitted):
        user_input = event.value
        user_input = user_input.strip().lower()
        
        if user_input == "/exit":
            self.exit()
            return

        keyword, argument = commands_input(user_input)

        # Check if the keyword is clear then clear the screen and return early. 
        if keyword == "/clear":
            self.query_one("#main_display").update("Search a Pokémon to view its information.")
            # self.query_one("#pokemon_card", PokemonCard).show_card("Seems like its been a while....")
            event.input.value = ""
            return 
    
        if keyword == "/info":
            self.query_one("#main_display").update("Hi, I'm Tushar. I built Pocket-Dex to learn Python, APIs, and \nclean code. The bugs weren't part of the Pokédex... \nthey just appeared naturally.") 
            event.input.value = ""
            return

        #if the keyword is not clear or exit continue with this program.
        pokemon_data = get_data(keyword, argument)     
    
        # If no data is found return early. else continue with the program.
        if pokemon_data == "404":
            self.query_one("#main_display").update("Invalid Input. \nPokemon not found.")
            event.input.value = ""
            return

        self.query_one("#pokemon_card", PokemonCard).show_card(pokemon_data)

        # Create the Rich display
        display = self.pokemon_display(pokemon_data)

        # Update the main display
        self.query_one("#main_display").update(display)
        
    
        event.input.value = ""


    # Creates the Rich UI only
    def pokemon_display(self, data):

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
    
class CliArt(Static):
    def on_mount(self):
        self.update("""   
    __________              __      __            ________          __  
    \______   \____   ____ |  | ___/  |_          \______ \   ____ |  | __
    |     ___/  _ \_/ ___\|  |/ /\   __\  ______  |    |  \_/ __ \|  |/ /
    |    |  (  <_> )  \___|    <  |  |   /_____/  |    `   \  ___/|    < 
    |____|   \____/ \___  >__|_ \ |__|           /_______  /\___  >__|_ \       
    """)    

class MainDisplay(Static):
    def show_message(self, text: str):
        self.update(text)

class UserInput(Static):
    def compose(self):
        yield Input(
            placeholder="Enter Pokémon name...",
            id="pokemon_input" 
        )
    
class APIStatus(Static):
    def on_mount(self):
        status =  api_status()
        self.update(status)
        
class PokemonCard(Static):
    def on_mount(self):
        self.update(
            Panel(
                "Search a Pokémon...",
                title="Pokémon Card"
            )
        )



    def show_card(self, data, rarity="Common"):

        card = Table.grid(padding=1)
        card.add_column(justify="center")

        card.add_row(f"[bold yellow]{data['name'].upper()}[/]")
        card.add_row("")
        card.add_row(f"[cyan]Type:[/] {(data['types'])}")
        card.add_row("")
        card.add_row(f"[bold green]★ {rarity}[/]")

        self.update(
            Panel(
                Align.center(card),
                title="Pokémon Card",
                border_style=self.get_border(rarity),
            )
        )

    def get_border(self, rarity):

        borders = {
            "Common": "white",
            "Rare": "blue",
            "Epic": "magenta",
            "Legendary": "red",
            "Gold": "yellow",
        }

        return borders.get(rarity, "white")

class AuthorNotes(Static):
    def on_mount(self):
        commands_info = [
        "/help    Show all commands",
        "/search  Search Pokémon",
        "/random  Random Pokémon",
        "/clear   Clear screen",
        "/info    About Pocket-Dex",
        "/exit    Exit application",
        ]
        text = "\n".join(commands_info)
        self.update(text)

if __name__ == "__main__":
    app = layout_fucntion()
    app.run()

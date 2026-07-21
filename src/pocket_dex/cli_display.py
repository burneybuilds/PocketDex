# Modules import`s
from .poke_api import api_status
from .command import commands_input, get_data
from .display_formatter  import info_display, error_display, welcome_display, api_ok, api_nf

# Textual Modules Import
from textual.app import App, ComposeResult
from textual.widgets import Static, Input
from textual.containers import Vertical, Horizontal

# Rich Modules Import 
from rich.panel import Panel
from rich.align import Align
from rich.table import Table
from rich.text import Text
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
    def on_mount(self):
        self.query_one("#main_display").update(welcome_display())

    # Handles user input
    def on_input_submitted(self, event: Input.Submitted):
        user_input = event.value
        user_input = user_input.strip().lower()
    
        if user_input == "":
            error_message = error_display("Please enter a Pokémon name.")
            self.query_one("#main_display").update(error_message)
            event.input.value = ""
            return

        if user_input == "/exit":
            self.exit()
            return

        if user_input == "/clear":
            self.query_one("#main_display").update(self.welcome_display())
            event.input.value = ""
            return 
    
        if user_input == "/info":
            self.query_one("#main_display").update(info_display()) 
            event.input.value = ""
            return

        keyword, argument, argument2 = commands_input(user_input)

        #if the keyword is not clear or exit continue with this program.
        pokemon_data, history = get_data(keyword, argument, argument2)     
    
        # If no data is found return early. else continue with the program.
        if pokemon_data == "invalid Keyword":
            error_message = error_display("Oops! I don't recognize that command.")
            self.query_one("#main_display").update(error_message)
            event.input.value = ""
            return
        elif pokemon_data == "PK not found":
            error_message = error_display("Pokémon not found.")
            self.query_one("#main_display").update(error_message)
            event.input.value = ""
            return
        elif pokemon_data == "Compare_fail":
            error_message = error_display("Compare requires two Pokémon names.")
            self.query_one("#main_display").update(error_message)
            event.input.value = ""
            return
        else:
            # self.query_one("#pokemon_card", PokemonCard).show_card(pokemon_data)
            # Create the Rich display
            # display = self.pokemon_display(pokemon_data)
            # Update the main display
            self.query_one("#main_display").update(pokemon_data)
        
        event.input.value = ""


    
class CliArt(Static):
    def on_mount(self):
        logo = Text(
r"""__________              __      __            ________          __
\______   \____   ____ |  | ___/  |_          \______ \   ____ |  | __
|     ___/  _ \_/ ___\|  |/ /\   __\  ______  |    |  \_/ __ \|  |/ /
|    |  (  <_> )  \___|    <  |  |   /_____/  |    `   \  ___/|    <
|____|   \____/ \___  >__|_ \ |__|           /_______  /\___  >__|_ \
                    \/     \/                      \/     \/
""",
            style="white",
        )

        self.update(
            Align.center(
                Panel.fit(
                    logo,
                    border_style="grey50",
                    subtitle="[grey70]@author:[/grey70] [bright_white]Albert[/bright_white]",
                    subtitle_align="right",
                    padding=(0, 1),
                ),
                vertical="middle",
            )
        )
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
    status =  api_status()    
    if status == "200":
        def on_mount(self):
            self.update(api_ok())
    else:
        def on_mount(self):
            self.update(api_nf())
        
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
        table = Table.grid(padding=(0, 2))
        table.add_column(style="bold cyan", no_wrap=True)
        table.add_column(style="white")

        table.add_row("/help",    "Show all commands")
        table.add_row("/search",  "Search a Pokémon")
        table.add_row("/random",  "Random Pokémon")
        table.add_row("/compare", "Compare two Pokémon")
        table.add_row("/types",   "Browse Pokémon types")
        table.add_row("/clear",   "Clear the screen")
        table.add_row("/info",    "About Pocket-Dex")
        table.add_row("/exit",    "Exit Pocket-Dex")

        self.update(
            Panel(
                table,
                title="[bold yellow]Quick Commands[/bold yellow]",
                border_style="grey50",
                padding=(0, 1),
            )
        )

if __name__ == "__main__":
    app = layout_fucntion()
    app.run()

from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.containers import Vertical, Horizontal
from textual.widgets import Static, Input, Button
from command import commands_input, help
import parser
import os
import random


class layout_fucntion(App):
    CSS_PATH = "styles\layout.tcss"

    def compose(self) -> ComposeResult:
        with Horizontal(): # splits screen into left and right
            with Vertical(id="left"):  # This divides the left screen into 3 Parts.
                yield CliArt()
                yield MainDisplay(id="main_display")
                yield UserInput()

            with Vertical(id="right"): # This divides the right screen into 3 Parts.
                yield APIStatus()
                yield RecentSearches()
                yield AuthorNotes()
    
    # This fucntion binds the input with the main display.
    def on_input_submitted(self, event: Input.Submitted):
        pokemon_name = event.value  # events get the value from the user and stores it to pokemon_name.
        keyword, argument = commands_input(pokemon_name) 
        data = self.get_data(keyword , argument)
        text = f"""
            Name: {data['name']}
            HP: {data['hp']}
            Attack: {data['attack']}
            Defense: {data['defense']}
            """
        self.query_one("#main_display").update(text) # Find the widget which have the id of main_display.
        event.input.value = "" # Clear the input box after you press enter 
    
    def get_data(self, keyword, pokemon_name):
        if keyword == "/search":
            data = parser.parser_data(pokemon_name)
            if data == "Not Found":
                print("Invalid Input.")
            return data
        elif keyword == "/random":
            pokemon_id = random.randint(1, 1025)
            data = parser.parser_data(str(pokemon_id))
            return data
        elif keyword == "/clear":
            os.system("cls" if os.name == "nt" else "clear")
        elif keyword == "/exit":
            print("Bye...")
            os.system("cls" if os.name == "nt" else "clear")
        elif keyword == "/help":
            info = help()
            for i in info:
                print(i)
        elif keyword == "/info":
            pass
           # about_me()
    

class CliArt(Static):
    def on_mount(self):
        self.update("""    __________              __      __            ________          __  
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
        self.update("🟢 PokeAPI Online")


class RecentSearches(Static):
    pass


class AuthorNotes(Static):
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


if __name__ == "__main__":
    app = layout_fucntion()
    app.run()




"""
This is the legacy pannel of the cli display using rich Lib but then it have less fucntions so i changes to Textual
"""
# This fucntion is like the monitor or the cli app so.
# def layout_fucntion():
#     layout = Layout()
#     layout.split_column(
#     Layout(name="big-left"),
#     )
#     layout["big-left"].split_row(
#     Layout(name="left", ratio=3),
#     Layout(name="right", ratio=1),
#     )
#     layout["left"].split_column(
#     Layout(name="cli-art", ratio=2),
#     Layout(name="main-display", ratio=6),
#     Layout(name="input-box", ratio=1),
#     )
#     layout["right"].split_column(
#     Layout(name="api-status", ratio=1),
#     Layout(name="recent_search",ratio=5),
#     Layout(name="extra-info", ratio=3),
#     )

#     layout["cli-art"].update(cli_art())
#     layout["extra-info"].update(random_info())
#     print(layout)
#     # layout["api-status"].update(api_status())
     
# layout_fucntion()
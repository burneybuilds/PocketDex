from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.containers import Vertical, Horizontal
from textual.widgets import Static, Input, Button
from .command import commands_input
from src import parser
import os
import random
from .poke_api import api_status


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
                yield AuthorNotes()
                yield RecentSearches()
    
    # This fucntion binds the input with the main display.
    def on_input_submitted(self, event: Input.Submitted):
        pokemon_name = event.value  # events get the value from the user and stores it to pokemon_name.
        keyword, argument = commands_input(pokemon_name) 
        data = self.get_data(keyword , argument)
        text = f"""
            ID: {data['id']}
            Name: {data['name']}
            Height: {data['height']}
            Weight: {data['weight']}
            Types: {data['types']}
            Abilities: {data['abilities']}

            HP: {data['hp']}
            Attack: {data['attack']}
            Defense: {data['defense']}
            Special Attack: {data['special_attack']}
            Special Defense: {data['special_defense']}
            Speed: {data['pokemon_speed']}

            Status: {data['status']}
            Moves: {data['moves']}
            Description: {data['description']}
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
        

class RecentSearches(Static):
    pass



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
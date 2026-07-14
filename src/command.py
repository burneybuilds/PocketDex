import random

from src import parser
from src import poke_api
from src import display_formatter
from src.history_handler import handle_input

# Take input from the user and divide the input into two part.
def commands_input(user_input):
    parts = user_input.split(maxsplit=1)

    keyword = parts[0]
    argument = parts[1] if len(parts) > 1 else None

    return keyword, argument
    

def get_data(keyword ,argument): 
    
    if poke_api.check_endpoint(argument) == False and keyword != "/random" or keyword != "/type":
        return "404", None

    if keyword == "/search":
        
        data = parser.parser_data(argument)
        recent_searchs = handle_input(data)
        display = display_formatter.search_pokemon_display(data)
        return display, recent_searchs
    
    elif keyword == "/random":
        
        pokemon_id = random.randint(1, 1025)
        data = parser.parser_data(str(pokemon_id))
        recent_searchs = handle_input(data)
        display = display_formatter.search_pokemon_display(data)
        return display, recent_searchs
    
    elif keyword == "/type":
        data = parser.prase_by_type(argument)
        display = display_formatter.type_pokemone_display(data)
        return display, None
    
    elif keyword == "/help":
        info = help()
        for i in info:
            print(i)

    else:
        return "404"


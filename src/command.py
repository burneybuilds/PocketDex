import random

from src import parser
from src import poke_api
from src import display_formatter
from src.history_handler import handle_input
from src.compare import get_parse_data

# Take input from the user and divide the input into two part.
def commands_input(user_input):
    parts = user_input.split(maxsplit=1)

    keyword = parts[0]
    argument = parts[1] if len(parts) > 1 else None

    return keyword, argument
    

def get_data(keyword ,argument): 
    
    keyword_list = ["/search", "/random", "/type" , "/compare", "/help"]

    if keyword not in keyword_list:
        return "404", None
    
    if keyword == "/search":
        
        if poke_api.check_endpoint(argument) == False:
            return "404", None
        
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
    
    elif keyword == "/compare":
        pokemon_1, pokemon_2 = get_parse_data()
        pass

    elif keyword == "/help":
        info = help()
        for i in info:
            print(i)

    else:
        return "404", None


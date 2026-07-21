import random

from . import parser
from . import poke_api
from . import display_formatter
from .history_handler import handle_input
from .compare import compare_engien

# Take input from the user and divide the input into two part.
def commands_input(user_input):
    parts = user_input.split(maxsplit=2)

    keyword = parts[0]
    argument = parts[1] if len(parts) > 1 else None
    argument2 = parts[2] if len(parts) > 2 else None
    return keyword, argument, argument2
    

def get_data(keyword ,argument, argument2): 
    
    keyword_list = ["/search", "/random", "/type" , "/compare", "/help"]

    if keyword not in keyword_list:
        return "invalid Keyword", None, None
    
    if keyword == "/search":
        
        if poke_api.check_endpoint(argument) == False:
            return "PK not found", None, None
        
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
        display = display_formatter.type_pokemon_display(data)
        return display, None
    
    elif keyword == "/compare":
        if argument == None or argument2 == None:
            return "Compare_fail" , None
        compare_result, status_1_stats, status_2_stats = compare_engien(argument , argument2)
        display = display_formatter.compare_display(status_1_stats, status_2_stats, compare_result)
        return display, None
    
    elif keyword == "/help":
        info = help()
        for i in info:
            print(i)

    else:
        return "404", None


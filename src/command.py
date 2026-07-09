import random

from src import parser
from src import poke_api

# Take input from the user and divide the input into two part.
def commands_input(user_input):
    parts = user_input.split(maxsplit=1)

    keyword = parts[0]
    argument = parts[1] if len(parts) > 1 else None

    return keyword, argument
    

def get_data(keyword ,pokemon_name): 
    
    if poke_api.check_endpoint(pokemon_name) == False:
        return "404"

    if keyword == "/search":
        data = parser.parser_data(pokemon_name)
        return data 
    elif keyword == "/random":
        pokemon_id = random.randint(1, 1025)
        data = parser.parser_data(str(pokemon_id))
        return data
        
    elif keyword == "/help":
        info = help()
        for i in info:
            print(i)

    else:
        return "404"
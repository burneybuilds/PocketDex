import os
import poke_api

commands_info = [
    "/help : Show all available commands.",
    "/search : Search for a Pokémon by name or Pokédex ID. Example: /search pikachu",
    "/random : Display a random Pokémon.",
    "/clear : Clear the terminal screen.",
    "/info : Show information about Pocket-Dex.",
    "/exit : Exit the application."
]

def search_pokemon(pokemon_name):
    response, extra_data, pokemon_name = poke_api.get_pokemon_by_name(pokemon_name)
    return response, extra_data, pokemon_name

def random_pokemon():
    response, extra_data, pokemon_name = poke_api.random_pokemon_by_id()
    return response, extra_data, pokemon_name

def help():
    return commands_info

def commands_input():
    user_input = input("<Pocket-Dex> ")

    parts = user_input.split(maxsplit=1)

    keyword = parts[0]
    argument = parts[1] if len(parts) > 1 else None

    return keyword, argument
        

    # This is one of my failed trys of keepign everything in one fucntion big brain me .
    # if not user_input == "/search":
    #     print("No... Wirte /search pikachu or /search 25")
    #     continue

    # if keyword == "/search":
    #     response, extra_data, pokemon_name = poke_api.get_pokemon_by_name(pokemon_name)
    #     return response, extra_data, pokemon_name, keyword, None
    # elif keyword == "/random":
    #     response, extra_data, pokemon_name = poke_api.random_pokemon_by_id()
    #     return response, extra_data, pokemon_name, keyword , None
    # elif keyword == "/clear":
    #     return None, None, None, keyword , None# I have no idea what it does.
    # elif keyword  == "/exit":
    #     return None, None, None, keyword , None
    # elif keyword == "/help":
    #     return None, None, None, keyword , commands
    # elif keyword == "/info":
    #     return about_me()
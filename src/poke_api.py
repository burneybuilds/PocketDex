import random
import requests as rq

"""
Fetches Pokémon information from the PokeAPI.

This function sends HTTPS GET requests to two PokeAPI endpoints:
1. /pokemon/         -> General Pokémon data.
2. /pokemon-species/ -> Species-specific information.

Returns:
    tuple:
        (pokemon_data, extra_data) on success.

        ("Not Found", None) if the Pokémon does not exist.

        ("404", None) if an HTTP-related error occurs.
"""
def get_pokemon_by_name(pokemon_name):
    try:
        pokemon_data = rq.get(
            "https://pokeapi.co/api/v2/pokemon/"+pokemon_name
        ).json()
        extra_data = rq.get(
            "https://pokeapi.co/api/v2/pokemon-species/"+pokemon_name
        ).json()
        return pokemon_data, extra_data, pokemon_name
    # Triggered when the requested Pokémon cannot be found, usually because
    # the user entered an invalid or misspelled name.
    except rq.exceptions.JSONDecodeError:
        return "Not Found", None, None
    # This gets called when there is a network connection issue. 
    except rq.exceptions.HTTPError: 
        return "404", None, None


"""
Fetches a random Pokémon from the PokeAPI.

This function uses the same PokeAPI endpoints as
get_pokemon_by_name(). See lines 8–10 for more information.

Returns:
    tuple:
        (pokemon_data, pokemon_extra, pokemon_id) on success.

        "Unable to connect to the server." if an HTTP-related error occurs.
"""
def random_pokemon_by_id():
    pokemon_id = random.randint(1, 1025)
    pokemon_id = str(pokemon_id)
    try:
        pokemon_data = rq.get(
            "https://pokeapi.co/api/v2/pokemon/"+pokemon_id
        ).json()
        pokemon_extra = rq.get(
            "https://pokeapi.co/api/v2/pokemon-species/"+pokemon_id
        ).json()
        return pokemon_data, pokemon_extra, pokemon_id
    # Triggered when the application is unable to communicate with the API.
    except rq.exceptions.HTTPError:
        return "Unable to conect to the server." 
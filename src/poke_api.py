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
    request_url_main = rq.get(
            "https://pokeapi.co/api/v2/pokemon/"+pokemon_name
        )
    request_extra_data = rq.get(
        "https://pokeapi.co/api/v2/pokemon-species/"+pokemon_name
    )
    
    try:
        pokemon_data = request_url_main.json()
        extra_data = request_extra_data.json()
        return pokemon_data, extra_data, pokemon_name
    # Triggered when the user entered an invalid or misspelled name.
    except rq.exceptions.JSONDecodeError:
        return "Not Found", None, None
    # This gets called when there is a network connection issue. 
    except rq.exceptions.HTTPError: 
        return "404", None, None
    

def api_status():
    up_time = rq.get("https://pokeapi.co/api/v2/pokemon/")
    if up_time.status_code == 200:
        return "🟢 Online"
    else:
        return "🔴 OFFLINE"
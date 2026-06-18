import requests

def main():
    responce = get_pokemon()
    name = responce["name"]
    height = responce["height"]
    type_name = responce["types"][0]["type"]["name"]
    print(f"Name: {name}")
    print(f"Height: {height}")
    print(f"Type: {type_name}")

def user_input():
    pokemon = input("Enter the Name of the Pokemon: ").strip().title()
    if pokemon.isdigit():
        return "Invalid Name."
    else:
        return pokemon

def get_pokemon():
    url = requests.get("https://pokeapi.co/api/v2/pokemon/")
    if url.status_code == 200:
        pokemon_name = user_input()
        request_url = "https://pokeapi.co/api/v2/pokemon/" + pokemon_name
        response = requests.get(request_url) # just for debugging
        data = response.json()
        return data
    else:
        return "Invalid"


main()
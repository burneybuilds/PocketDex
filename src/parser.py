from src import poke_api

def parse_basic_info(pokemon_data):
    pokemon_id = pokemon_data["id"]
    name = pokemon_data["name"]
    pokemone_height = pokemon_data["height"]
    types = pokemon_data["types"]
    abilities = pokemon_data["abilities"]
    weight = pokemon_data["weight"]

    pokemon_type = []
    for t in types:
        pokemon_type.append(t["type"]["name"])
        all_types = " / ".join(pokemon_type)
            
    pokemon_abilities = []
    for a in abilities:
        pokemon_abilities.append(a["ability"]["name"])
        all_abilities = " / ".join(pokemon_abilities)

    basic_data ={
        "id": pokemon_id,
        "name": name,
        "height": pokemone_height,
        "weight": weight,
        "types": all_types,
        "abilities": all_abilities,
    }

    return basic_data

    
def parse_basic_stats(pokemon_data):
    hp = pokemon_data["stats"][0]["base_stat"]
    attack = pokemon_data["stats"][1]["base_stat"]
    defense = pokemon_data["stats"][2]["base_stat"]
    special_attack = pokemon_data["stats"][3]["base_stat"]
    special_defense = pokemon_data["stats"][4]["base_stat"]
    pokemon_speed = pokemon_data["stats"][5]["base_stat"]

    basic_stats={
        "hp": hp,
        "attack": attack,
        "defense": defense,
        "special_attack": special_attack,
        "special_defense": special_defense,
        "pokemon_speed": pokemon_speed,
    }

    return basic_stats


def parse_status(pokemon_extra_data):
    is_legendary_status = pokemon_extra_data["is_legendary"]
    is_mythical_status = pokemon_extra_data["is_mythical"]

    status = "Normal Pokemon"
    if is_legendary_status == True:
        status = "Legendary Pokemon"
    elif is_mythical_status == True:
        status = "Mytical Pokemon"
    else:
        status  # Still stronger than my first Python projects.

    return status

def parse_description(pokemon_extra_data):
    discription = pokemon_extra_data["flavor_text_entries"]
    for d in discription:
        if d["language"]["name"] == "en":
            pokemo_info = d["flavor_text"] # My Japanese DLC hasn't been installed yet

    pokemo_info = pokemo_info.replace("\n", " ")
    pokemo_info = pokemo_info.replace("\f", " ") # The API likes hiding surprise characters.
    
    return pokemo_info


def parse_moves(pokemon_data):
    moves = []
    all_moves = pokemon_data["moves"]
    for m in all_moves:
        moves.append(m["move"]["name"])
    
    temp_list = []
    for i in range(5):
        temp_list.append(moves[i])
    
    pokemon_moves = " , ".join(temp_list)

    return pokemon_moves


def parser_data(pokemon_name):
    response, extra_data, pokemon_name = poke_api.get_pokemon_by_name(pokemon_name)
    
    if response == "Not Found":
        return "Not Found"

    basic_data = parse_basic_info(response)
    basic_stats = parse_basic_stats(response)
    status = parse_status(extra_data)
    pokemon_moves = parse_moves(response)
    discription =parse_description(extra_data)
    
    data = {
    "id": basic_data["id"],
    "name": basic_data["name"],
    "height": basic_data["height"],
    "weight": basic_data["weight"],
    "types": basic_data["types"],
    "abilities": basic_data["abilities"],

    "hp": basic_stats["hp"],
    "attack": basic_stats["attack"],
    "defense": basic_stats["defense"],
    "special_attack": basic_stats["special_attack"],
    "special_defense": basic_stats["special_defense"],
    "pokemon_speed": basic_stats["pokemon_speed"],

    "description": discription,
    "status": status,
    "moves": pokemon_moves,
    }
    
    return data
    
    # s_history = [] # empty list 
    # s_history.append(pokemon_name)  # Future me will forget what I searched.
    # searchs = ", ".join(s_history)
import poke_api
import command


def parser_data(pokemon_name):
    response, extra_data, poke_name = poke_api.get_pokemon_by_name(pokemon_name)
    
    if response == "Not Found":
        return "Not Found"
    
    pokemon_id = response["id"]
    name = response["name"]
    pokemone_height = response["height"]
    types = response["types"]
    abilities = response["abilities"]
    weight = response["weight"]
            
    hp = response["stats"][0]["base_stat"]
    attack = response["stats"][1]["base_stat"]
    defense = response["stats"][2]["base_stat"]
    special_attack = response["stats"][3]["base_stat"]
    special_defense = response["stats"][4]["base_stat"]
            
    pokemon_type = []
    for t in types:
        pokemon_type.append(t["type"]["name"])
        all_types = " / ".join(pokemon_type)
            
    pokemon_abilities = []
    for a in abilities:
        pokemon_abilities.append(a["ability"]["name"])
        all_abilities = " / ".join(pokemon_abilities)
    
    discription = extra_data["flavor_text_entries"]
    for d in discription:
        if d["language"]["name"] == "en":
            pokemo_info = d["flavor_text"] # My Japanese DLC hasn't been installed yet

    pokemo_info = pokemo_info.replace("\n", " ")
    pokemo_info = pokemo_info.replace("\f", " ") # The API likes hiding surprise characters.

    is_legendary_status = extra_data["is_legendary"]
    is_mythical_status = extra_data["is_mythical"]

    status = "Normal Pokemon"
    if is_legendary_status == True:
        status = "Legendary Pokemon"
    elif is_mythical_status == True:
        status = "Mytical Pokemon"
    else:
        status  # Still stronger than my first Python projects.

    data = {
    "id": pokemon_id,
    "name": name,
    "height": pokemone_height,
    "weight": weight,
    "types": all_types,
    "abilities": all_abilities,
    "hp": hp,
    "attack": attack,
    "defense": defense,
    "special_attack": special_attack,
    "special_defense": special_defense,
    "description": pokemo_info,
    "status": status,}
    
    return data
    
    # s_history = [] # empty list 
    # s_history.append(pokemon_name)  # Future me will forget what I searched.
    # searchs = ", ".join(s_history)
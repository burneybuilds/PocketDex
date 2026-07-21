from .parser import parser_data
from .poke_api import get_pokemon_by_name
 
def compare(num1 , num2):
    if num1 > num2:
        return 1
    else:
        return 0

def compare_hp(stats1, stats2):
    hp_1 = stats1["hp"]
    hp_2 = stats2["hp"]
    return compare(hp_1, hp_2)
    
def compare_attack(stats1, stats2):
    attack_1 = stats1["attack"]
    attack_2 = stats2["attack"]
    return compare(attack_1, attack_2)

def compare_defense(stats1, stats2):
    defens_1 = stats1["defense"]
    defens_2 = stats2["defense"]
    return compare(defens_1, defens_2)

def compare_special_attack(stats1, stats2):
    special_attack_1 = stats1["special_attack"]
    special_attack_2 = stats2["special_attack"]
    return compare(special_attack_1, special_attack_2)

def compare_special_defense(stats1, stats2):
    special_defense_1 = stats1["special_defense"]
    special_defense_2 = stats2["special_defense"]
    return compare(special_defense_1 ,special_defense_2)
    
def compare_speed(stats1, stats2):
    speed_1= stats1["pokemon_speed"]
    speed_2 = stats2["pokemon_speed"]
    return compare(speed_1, speed_2)

def compare_engien(data,  data2):
    status_1 = parser_data(data)
    status_2 = parser_data(data2)

    status_1_stats = {
        "name" : status_1["name"],
        "hp": status_1["hp"],
        "attack": status_1["attack"],
        "defense": status_1["defense"],
        "special_attack": status_1["special_attack"],
        "special_defense": status_1["special_defense"],
        "pokemon_speed": status_1["pokemon_speed"],
    }
    status_2_stats = {
        "name" : status_2["name"],
        "hp": status_2["hp"],
        "attack": status_2["attack"],
        "defense": status_2["defense"],
        "special_attack": status_2["special_attack"],
        "special_defense": status_2["special_defense"],
        "pokemon_speed": status_2["pokemon_speed"],
    }
    pokemone_1 = []
    pokemone_2 = []
    
    functions = [compare_hp,
                compare_attack,
                compare_defense,
                compare_special_attack,
                compare_special_defense,
                compare_speed,
                ]
    for f in functions:
        point = f(status_1, status_2)
        if point == 1:
            pokemone_1.append(point)
        else:
            pokemone_2.append(point)

    if len(pokemone_1) > len(pokemone_2):
        return F"{status_1["name"]} Is stronger.", status_1_stats, status_2_stats
    elif len(pokemone_1) < len(pokemone_2):
        return F"{status_2["name"]} Is stronger.", status_1_stats, status_2_stats
    else:
        return "Both Pokemon are same." , status_1_stats, status_2_stats
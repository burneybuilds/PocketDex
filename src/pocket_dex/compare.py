from .parser import parser_data
from .poke_api import get_pokemon_by_name

def get_parse_data(pokemon_name_1, pokemon_name_2):    
    pokemon_one_data = get_pokemon_by_name(pokemon_name_1)
    pokemon_two_data = get_pokemon_by_name(pokemon_name_2)

    pokemone1 = parser_data(pokemon_one_data)
    pokemone2 = parser_data(pokemon_two_data)

    return pokemone1, pokemone2 

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

def compare_engien():
    status_1 = parse_basic_stats(data_1)
    status_2 = parse_basic_stats(data_2)

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
        return F"{pokemone_name1} Is stronger."
    elif len(pokemone_1) < len(pokemone_2):
        return F"{pokemone_name2} Is stronger."  
    else:
        return "Both Pokemon are same." 
from pocket_dex.poke_api import api_status, get_pokemon_by_type, get_pokemon_by_name

def test_api():
    assert api_status() == "200"

def test_api_type_endpoint():
    #assert get_pokemon_by_type("fire") == True
    assert get_pokemon_by_type(" ") == "Not Found"

def test_api_search_endpoint():
    #assert get_pokemon_by_name("pikachu") == True
    assert get_pokemon_by_name("pika") == ("Not Found", None, None)

def test_invalid_name():
    assert get_pokemon_by_name(" ") == ("Not Found", None, None)
    assert get_pokemon_by_name("-23") ==  ("Not Found", None, None)
from src.parser import parse_description
from src.parser import parse_basic_stats
from src.parser import parse_basic_info
from src.parser import prase_by_type
import requests as rq

response_url = rq.get("https://pokeapi.co/api/v2/pokemon/pikachu").json()
response_url2 = rq.get("https://pokeapi.co/api/v2/pokemon-species/pikachu").json()

def test_description():
    assert parse_description(response_url2) == (
        "Possesses cheek sacs in which it stores electricity. This clever forest-dweller roasts tough berries with an electric shock before consuming them."
    )

def test_basic_stats():
    data = parse_basic_stats(response_url)
    assert data["hp"] == 35
    assert data["attack"] == 55
    assert data["defense"] == 40
    assert data["special_attack"] == 50
    assert data["special_defense"] == 50
    assert data["pokemon_speed"] == 90


def test_basic_info():
    data = parse_basic_info(response_url) 
    assert data["id"] == 25
    assert data["name"] == "pikachu"
    assert data["height"] == 4
    assert data["weight"] == 60
    assert data["types"] == "electric"
    assert data["abilities"] == "static / lightning-rod"

# def test_type_info():
#     assert prase_by_type({"name" : "pikachu"}) == "pikachu"


def test_status():
    pass

def test_moves():
    pass

    
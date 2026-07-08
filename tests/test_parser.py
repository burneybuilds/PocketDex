from src.parser import parse_description
from src.parser import parse_basic_stats
from src.parser import parse_basic_info
import requests as rq

def test_description():
    response = rq.get("https://pokeapi.co/api/v2/pokemon-species/pikachu").json()
    assert parse_description(response) == (
        "Possesses cheek sacs in which it stores electricity. This clever forest-dweller roasts tough berries with an electric shock before consuming them."
    )

def test_basic_stats():
    response = rq.get("https://pokeapi.co/api/v2/pokemon/pikachu").json()
    data = parse_basic_stats(response)
    assert data["hp"] == 35
    assert data["attack"] == 55
    assert data["defense"] == 40
    assert data["special_attack"] == 50
    assert data["special_defense"] == 50
    assert data["pokemon_speed"] == 90


def test_basic_info():
    response = rq.get("https://pokeapi.co/api/v2/pokemon/pikachu").json()
    data = parse_basic_info(response) 
    assert data["id"] == 25
    assert data["name"] == "pikachu"
    assert data["height"] == 4
    assert data["weight"] == 60
    assert data["types"] == "electric"
    assert data["abilities"] == "static / lightning-rod"

def test_status():
    pass

def test_moves():
    pass

    
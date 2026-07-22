import requests as rq

from pocket_dex.parser import (
    parse_basic_info,
    parse_basic_stats,
    parse_status,
    parse_description,
    parse_moves,
    prase_by_type,
    parser_data,
)

response = rq.get("https://pokeapi.co/api/v2/pokemon/pikachu").json()
species = rq.get("https://pokeapi.co/api/v2/pokemon-species/pikachu").json()


def test_description():
    assert parse_description(species) == (
        "Possesses cheek sacs in which it stores electricity. "
        "This clever forest-dweller roasts tough berries with an electric shock before consuming them."
    )


def test_basic_stats():
    data = parse_basic_stats(response)

    assert data["hp"] == 35
    assert data["attack"] == 55
    assert data["defense"] == 40
    assert data["special_attack"] == 50
    assert data["special_defense"] == 50
    assert data["pokemon_speed"] == 90


def test_basic_info():
    data = parse_basic_info(response)

    assert data["id"] == 25
    assert data["name"] == "pikachu"
    assert data["height"] == 4
    assert data["weight"] == 60
    assert data["types"] == "electric"
    assert data["abilities"] == "static / lightning-rod"


def test_status():
    assert parse_status(species) == "Normal Pokemon"


def test_moves():
    moves = parse_moves(response)

    assert isinstance(moves, str)
    assert len(moves) > 0


def test_parser_data():
    data = parser_data("pikachu")

    assert data["name"] == "pikachu"
    assert data["id"] == 25
    assert data["hp"] == 35
    assert "description" in data
    assert "moves" in data


def test_parse_by_type():
    pokemon = prase_by_type("fire")

    assert isinstance(pokemon, list)
    assert len(pokemon) > 0
    assert "charmander" in pokemon
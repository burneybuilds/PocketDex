from pocket_dex.poke_api import (
    api_status,
    get_pokemon_by_name,
    get_pokemon_by_type,
    check_endpoint,
)


def test_api_status():
    assert api_status() == "200"


def test_get_pokemon():
    pokemon, species, name = get_pokemon_by_name("pikachu")

    assert pokemon["name"] == "pikachu"
    assert species["name"] == "pikachu"
    assert name == "pikachu"


def test_invalid_pokemon():
    assert get_pokemon_by_name("pika") == ("Not Found", None, None)
    assert get_pokemon_by_name(" ") == ("Not Found", None, None)
    assert get_pokemon_by_name("-23") == ("Not Found", None, None)


def test_get_type():
    data = get_pokemon_by_type("fire")

    assert "pokemon" in data
    assert len(data["pokemon"]) > 0


def test_invalid_type():
    assert get_pokemon_by_type(" ") == "Not Found"


def test_check_endpoint():
    assert check_endpoint("pikachu") is True


def test_check_endpoint_invalid():
    assert check_endpoint("pika") is False
    assert check_endpoint(" ") is False
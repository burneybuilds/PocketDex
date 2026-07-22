import pytest
from pocket_dex.compare import (
    compare,
    compare_hp,
    compare_attack,
    compare_defense,
    compare_special_attack,
    compare_special_defense,
    compare_speed,
    compare_engien,
)


sample_1 = {
    "name": "pikachu",
    "hp": 35,
    "attack": 55,
    "defense": 40,
    "special_attack": 50,
    "special_defense": 50,
    "pokemon_speed": 90,
}

sample_2 = {
    "name": "bulbasaur",
    "hp": 45,
    "attack": 49,
    "defense": 49,
    "special_attack": 65,
    "special_defense": 65,
    "pokemon_speed": 45,
}


def test_compare():
    assert compare(10, 5) == 1
    assert compare(5, 10) == 0
    assert compare(5, 5) == 0


def test_compare_hp():
    assert compare_hp(sample_1, sample_2) == 0


def test_compare_attack():
    assert compare_attack(sample_1, sample_2) == 1


def test_compare_defense():
    assert compare_defense(sample_1, sample_2) == 0


def test_compare_special_attack():
    assert compare_special_attack(sample_1, sample_2) == 0


def test_compare_special_defense():
    assert compare_special_defense(sample_1, sample_2) == 0


def test_compare_speed():
    assert compare_speed(sample_1, sample_2) == 1


def test_compare_engine(monkeypatch):

    def fake_parser(name):
        if name == "pikachu":
            return sample_1
        return sample_2

    monkeypatch.setattr(
        "pocket_dex.compare.parser_data",
        fake_parser,
    )

    result, p1, p2 = compare_engien("pikachu", "bulbasaur")

    assert result == "bulbasaur Is stronger."
    assert p1["name"] == "pikachu"
    assert p2["name"] == "bulbasaur"
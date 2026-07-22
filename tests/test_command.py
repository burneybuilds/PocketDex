from rich.console import Group
from rich.columns import Columns

from pocket_dex.command import commands_input, get_data


def test_input():
    keyword, argument, _ = commands_input("/search pikachu")

    assert keyword == "/search"
    assert argument == "pikachu"


def test_single_input():
    keyword, argument, _ = commands_input("/search")

    assert keyword == "/search"
    assert argument is None


def test_invalid_command():
    data, _, _ = get_data("32432", None, None)

    assert data == "invalid Keyword"


def test_invalid_pokemon():
    data, _, _ = get_data("/search", "pika", None)

    assert data == "PK not found"


def test_random():
    display, history = get_data("/random", None, None)

    assert isinstance(display, Group)
    assert history is None


def test_type():
    display, history = get_data("/type", "fire", None)

    assert isinstance(display, Columns)
    assert history is None


def test_compare_missing_argument():
    data, _ = get_data("/compare", "pikachu", None)

    assert data == "Compare_fail"


def test_compare():
    display, history = get_data("/compare", "pikachu", "charizard")

    assert isinstance(display, Group)
    assert history is None
from src.command import commands_input
from src.command import get_data

def test_input():
    keyword, arugment = commands_input("/search pikachu")
    assert keyword == "/search"
    assert arugment =="pikachu"

def test_singal_input():
    keyword, arugment = commands_input("/search")
    assert keyword == "/search"
    assert arugment == None


# !! TO-DO need to to wrigth test for these two fucntion.
def test_check_radom():
    data, _ = get_data("/random", "")
    pass

def test_check_type():
    data, _ = get_data("/type", "fire")
    pass


# ? This test is no longer needed bacause now a formated ui is coming not raw data.
# def test_data():
#     data, _ = get_data("/random")
#     assert data["name"] == "pikachu"
#     assert data["id"] == 25

def test_invalid_command():
    data, _ = get_data("32432", "")
    assert data == "404"

def test_data_fail():
    data, _ = get_data("/search" ,"pika")
    assert data == "404", None

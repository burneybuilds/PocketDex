from src.command import commands_input
from src.command import get_data

def test_input():
    keyword, arugment = commands_input("/search pikachu")
    assert keyword == "/search"
    assert arugment =="pikachu"

def test_singal_input():
    keyword, arugment = commands_input("/search")
    assert keyword == "/search"
    assert arugment ==None

def test_data():
    data = get_data("/search" ,"pikachu")
    assert data["name"] == "pikachu"
    assert data["id"] == 25

def test_data_fail():
    data = get_data("/search" ,"pika")
    assert data == "404"
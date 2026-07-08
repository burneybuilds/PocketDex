from src.command import commands_input

def test_input():
    keyword, arugment = commands_input("/search pikachu")
    assert keyword == "/search"
    assert arugment =="pikachu"
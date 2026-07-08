from src.poke_api import api_status

def test_api():
    assert api_status() == "🟢 Online"
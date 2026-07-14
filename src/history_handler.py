import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
HISTORY_FILE_PATH = os.path.join(BASE_DIR, "history", "search_history.txt")


# I know this code is bad, but i will make it better later.
def handle_input(data):
    pokemon_name = data["name"]
    recent_searchs = []
    with open(HISTORY_FILE_PATH) as r:
        searches = r.read()
        

    if pokemon_name not in searches:
        with open(HISTORY_FILE_PATH, "a") as w:
            w.write(f"{pokemon_name}\n")


    with open(HISTORY_FILE_PATH) as r:
        searches_history = r.read()
        return searches_history
    
    
    return recent_searchs

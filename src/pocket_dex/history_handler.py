import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
HISTORY_FILE_PATH = os.path.join(BASE_DIR, "history", "search_history.txt")


# I know this code is bad, but i will make it better later.
def handle_input(data):
    pokemon_name = data["name"]
    recent_searchs = []
    with open(HISTORY_FILE_PATH, "r") as r:
        searches = r.read()
        

    if pokemon_name not in searches:
        with open(HISTORY_FILE_PATH, "a") as w:
            w.write(f"{pokemon_name}\n")


    with open(HISTORY_FILE_PATH, "r") as r:
        # searches_history = r.readline()
        for search in r:
            recent_searchs.append(search.replace("\n", ""))
        
        if len(recent_searchs) > 5:
            recent_searchs.pop(0)
    
    with open(HISTORY_FILE_PATH, "w") as file:
        for item in recent_searchs:
            file.write(item + "\n")
    
    return recent_searchs

def load_history():
    try:
        with open(HISTORY_FILE_PATH, "r") as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        return []


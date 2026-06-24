import requests
import os
import random 


def cli_art(): 
    print("██████   ██████   ██████ ██   ██ ███████ ████████       ██████  ███████ ██   ██")
    print("██   ██ ██    ██ ██      ██  ██  ██         ██          ██   ██ ██      ██  ██ ")
    print("██████  ██    ██ ██      █████   █████      ██    █████ ██   ██ █████   █████  ")
    print("██      ██    ██ ██      ██  ██  ██         ██          ██   ██ ██      ██  ██ ")
    print("██       ██████   ██████ ██   ██ ███████    ██          ██████  ███████ ██   ██")
    print("                                                                           V1.0")

def about_me():
        clear_screen()

        print("==========================================================================================")
        print("Hey, my name is Tushar.                                                                              ")
        print("You might be wondering why I made this project. To be honest, it started as a fun project while I was")
        print("learning Python. I wanted something practical where I could apply the concepts I was learning instead of")
        print("only solving coding exercises.")
        print("                                                                                                        ")
        print("PocketDex is one of my first Python projects, and it has helped me learn about APIs, functions, loops,")
        print("dictionaries, and user interaction. While it's still a work in progress, I'm excited to keep improving it and")
        print("adding new features over time.")
        print("")
        print("Thanks for checking it out!")
        print("==========================================================================================")

        input("\nPress Enter to return to the menu...")
        clear_screen() # Clear the screen after displaying.

def clear_screen(): #This Function Clear the screen.
    os.system("cls" if os.name == "nt" else "clear") # I have no idea what it does. 

# @ : This function takes the response from the API and displays it in a nice format.
def handle_search(): 
    while True: 
        response, extra_data, pokemon_name = get_pokemon_by_name()
        if response == "Exit": 
            clear_screen() 
            break
        elif response == "404": # No signal, no Pokémon. The internet gods said no.
            print()
            print("Could not connect to PokeAPI.")
            input("\nPress Enter to return to the menu...") 
            clear_screen()
            break
        elif response == "Not Found":
            print("No Pokemon With such Name Found.")
            input("\nPress Enter to return to the menu...")
            clear_screen()
            break
        # elif response == "Number":
        #     print("Invalid Input.")
        else: # show the ouput in a nice format.
            display_pokemon(response, extra_data, pokemon_name)

def get_pokemon_by_name():
    # history = [] 
    while True: # Runs a infinite loop until the user enters "1" to exit.
        pokemon = input("Enter the Name of the Pokemon/ID: ").strip().title() # Takes input and stores it in pokemon.
        if pokemon == "1":
            return "Exit", None, None 
        # elif pokemon.isdigit(): # Fun Fact the Guard Condition was stoping a feture, now you can serch pokemon by ID
        #     return "Number" 
        else:
            # url = requests.get("https://pokeapi.co/api/v2/pokemon/")
            pokemon_name = pokemon 
            try:
                request_url = "https://pokeapi.co/api/v2/pokemon/" + pokemon_name
                request_url1 = "https://pokeapi.co/api/v2/pokemon-species/" + pokemon_name
                pokemon_data = requests.get(request_url).json() 
                extra_data = requests.get(request_url1).json()
                # pokemon_data = response.json()
                # extra_data = response_extra.json()
                # history.append(pokemon)
                # s_history = " ".join(history)
                return pokemon_data, extra_data, pokemon
            except requests.RequestException:
                return "404", None, None
            except requests.exceptions.HTTPError:
                return "Not Found", None, None
            # if response.status_code ==  404:
            #     return "Data Not Found"
            # else:
            #     pokemon_data = response.json()  # Get the data from the api in the json format.
            #     return pokemon_data #Sends the json data to bridge fucntion to display the data in a nice format.


def random_pokemon_by_id():
    pokemon_id = random.randint(1, 1025)
    pokemon_id = str(pokemon_id)
    # Build both API endpoints because species information
    # and Pokémon stats come from different endpoints.
    request_url = "https://pokeapi.co/api/v2/pokemon/" + pokemon_id
    request_url1 = "https://pokeapi.co/api/v2/pokemon-species/" + pokemon_id
    try:
        pokemon_data = requests.get(request_url).json()
        pokemon_extra = requests.get(request_url1).json()
        # pokemon_data = response.json()
        # pokemon_extra = extra_data.json()
        display_pokemon(pokemon_data, pokemon_extra, pokemon_id)
        input("\nPress Enter to return to the menu...")
        clear_screen()
    except requests.RequestException:
        print("Could not connect to PokeAPI.") 
        input("\nPress Enter to return to the menu...")
        clear_screen()
        # if response.status_code == 200:                           # Old status-code handling kept for reference.
        #     display_pokemon(pokemon_data)                         # The current version uses try/except instead.
        #     input("\nPress Enter to return to the menu...")
        #     clear_screen()
        # elif response.status_code == 404:
        #     return "Connection Time-Out.""


s_history = [] # This needs to sit outside the fucntion or else it will get updated eveytime the fucntion is called.
def display_pokemon(response, extra_data, pokemon_name):
    pokemon_id = response["id"]
    name = response["name"]
    height = response["height"]
    types = response["types"]
    abilities = response["abilities"]
    weight = response["weight"]
            
    hp = response["stats"][0]["base_stat"]
    attack = response["stats"][1]["base_stat"]
    defense = response["stats"][2]["base_stat"]
    special_attack = response["stats"][3]["base_stat"]
    special_defense = response["stats"][4]["base_stat"]
            
    pokemon_type = []
    for t in types:
        pokemon_type.append(t["type"]["name"])
        all_types = " / ".join(pokemon_type)
            
    pokemon_abilities = []
    for a in abilities:
        pokemon_abilities.append(a["ability"]["name"])
        all_abilities = " / ".join(pokemon_abilities)
    
    discription = extra_data["flavor_text_entries"]
    for d in discription:
        if d["language"]["name"] == "en":
            pokemo_info = d["flavor_text"] # My Japanese DLC hasn't been installed yet

    pokemo_info = pokemo_info.replace("\n", " ")
    pokemo_info = pokemo_info.replace("\f", " ") # The API likes hiding surprise characters.

    is_legendary_status = extra_data["is_legendary"]
    is_mythical_status = extra_data["is_mythical"]

    status = ""
    if is_legendary_status == True:
        status = "Legendary Pokemon"
    elif is_mythical_status == True:
        status = "Mytical Pokemon"
    else:
        status = "Normal Pokemon" # Still stronger than my first Python projects.

    # s_history = [] # empty list 
    s_history.append(pokemon_name)  # Future me will forget what I searched.
    searchs = ", ".join(s_history)
    # search = " / ".join(s_historu).title # This code has been promoted to "historical artifact" status.
    #history = search_histoy()
    clear_screen()  # Every Pokédex deserves a dramatic entrance.
    cli_art()
    print("                                                                              ")
    print("= General Info ===============================================================")
    print("                                                                              ")
    print(f"| ID: {pokemon_id}                                      ") 
    print(f"| Name: {name}                                   ")    
    print(f"| Type: {all_types}                              ")
    print(f"| Abilities: {all_abilities}                     ")
    print(f"| Height: {height}                               ")
    print(f"| Weight: {weight}                               ")
    print("|                                                                            ")
    print(f"| Status : {status}                                                         ")
    print("                                                                              ")
    print("= Stats ======================================================================")
    print("                                                                              ")
    print(f"| HP : {hp}                                     ")                                       
    print(f"| Attack : {attack}                             ")           
    print(f"| Defense : {defense}                           ")
    print(f"| Special Attack : {special_attack}             ")
    print(f"| Special Defense : {special_defense}           ")
    print("                                                                              ")
    print(f"= Discription: {pokemo_info}")
    print("======================================================================")
    print(f"Recent Serches: {searchs}")
    print("======================================================================")
    print("1. Press 1 to go back || 2. Press 2 to Get More Info About the Pokemon")
    print()


def search_menu():
    while True: #Runs a infinite loop until the user enters "3" to exit.
        cli_art() # You can remove this if you want. 
        print("=======================")
        print("1. Search Pokemon (Name / ID)  ") 
        print("2. Random Pokemon              ")
        print("3. About Me                    ") 
        print("4. Exit                        ")
        print("=======================")
        user_choice = input("Enter your Choice: ") #Takes Input and stores it in user_choice.
        if user_choice == "1":  # Currently, 1 is string not a int and so the other.
            handle_search()
        elif user_choice == "2":
            random_pokemon_by_id()
        elif user_choice == "3":
            about_me() 
        elif user_choice == "4":
            clear_screen()
            break   
        else:
            print("Invalid Choice")
 
""" Info: 
An old idea that taught me something.
Search history originally lived here, but later moved into
display_pokemon() to reduce duplicate work and simplify the flow.
Keeping this around as a small reminder that code evolves."""
# def search_history()
    # # n , history = get_pokemon_by_name()
    # for h in history:
    #     print(h)
    # store = 5 
    # for _ in store:
    #     history = []
    #     _ , name = get_pokemon_by_name()
    #     if name == "Exit" or name == "Number" or name == "404":
    #         continue
    #     else:
    #         history.append(name)
    # recent_history = f"Recent: {history}"
    # return recent_history

def main():
    # Clear the screen before runing the program
    clear_screen()
    search_menu()

if __name__ == "__main__":
    main()
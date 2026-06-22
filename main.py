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
        response, Name = get_pokemon_by_name()
        if response == "Exit": 
            clear_screen() 
            break
        elif response == "404": 
            print("Could not connect to PokeAPI.") 
            break
        # elif response == "Number":
        #     print("Invalid Input.")
        else: # show the ouput in a nice format.
            display_pokemon(response, Name)

def get_pokemon_by_name():
    # history = [] 
    while True: # Runs a infinite loop until the user enters "1" to exit.
        pokemon = input("Enter the Name of the Pokemon/ID: ").strip().title() # Takes input and stores it in pokemon.
        if pokemon == "1":
            return "Exit", None
        # elif pokemon.isdigit(): # Fun Fact the Guard Condition was stoping a feture, now you can serch pokemon by ID
        #     return "Number" 
        else:
            # url = requests.get("https://pokeapi.co/api/v2/pokemon/")
            pokemon_name = pokemon 
            try:
                request_url = "https://pokeapi.co/api/v2/pokemon/" + pokemon_name
                response = requests.get(request_url) # just for debugging
                pokemon_data = response.json()
                # history.append(pokemon)
                # s_history = " ".join(history)
                return pokemon_data, pokemon
            except requests.RequestException:
                return "404"
            # if response.status_code ==  404:
            #     return "Data Not Found"
            # else:
            #     pokemon_data = response.json()  # Get the data from the api in the json format.
            #     return pokemon_data #Sends the json data to bridge fucntion to display the data in a nice format.


def random_pokemon_by_id():
    pokemon_id = random.randint(1, 1025)
    pokemon_id = str(pokemon_id)
    request_url = "https://pokeapi.co/api/v2/pokemon/" + pokemon_id
    try:
        response = requests.get(request_url)
        pokemon_data = response.json()
        display_pokemon(pokemon_data)
        input("\nPress Enter to return to the menu...")
        clear_screen()
    except requests.RequestException:
        print("Could not connect to PokeAPI.") 
        input("\nPress Enter to return to the menu...")
        clear_screen()
        # if response.status_code == 200:
        #     display_pokemon(pokemon_data)
        #     input("\nPress Enter to return to the menu...")
        #     clear_screen()
        # elif response.status_code == 404:
        #     return "Connection Time-Out.""


def display_pokemon(response, history):
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
    
    p_name = history
    s_historu = []
    s_historu.append(p_name)
    search = " / ".join(s_historu).title
    #history = search_histoy()
    clear_screen()
    cli_art()
    print("                                                                              ")
    print("= General Info ===============================================================")
    print("                                                                              ")
    print(f"| ID: {pokemon_id}                                       ") 
    print(f"| Name: {name}                                   ")    
    print(f"| Type: {all_types}                              ")
    print(f"| Abilities: {all_abilities}                     ")
    print(f"| Height: {height}                               ")
    print(f"| Weight: {weight}                               ")
    print("                                                                              ")
    print("= Stats ======================================================================")
    print("                                                                              ")
    print(f"| HP : {hp}                                     ")                                       
    print(f"| Attack : {attack}                             ")           
    print(f"| Defense : {defense}                           ")
    print(f"| Special Attack : {special_attack}             ")
    print(f"| Special Defense : {special_defense}           ")
    print("                                                                              ")
    print(search)

def search_menu():
    while True: #Runs a infinite loop until the user enters "3" to exit.
        cli_art() # You can remove this if you want. 
        print("=======================")
        print("1. Search Pokemon (Name / ID)  ") 
        print("2. Random Pokemon ")
        print("3. About Me ") 
        print("4. Recent Searches")
        print("5. Exit     ")
        print("=======================")
        user_choice = input("Enter your Choice: ") #Takes Input and stores it in user_choice.
        if user_choice == "1":  # Currently, 1 is string not a int and so the other.
            handle_search()
        elif user_choice == "2":
            random_pokemon_by_id()
        elif user_choice == "3":
            about_me() 
        elif user_choice == "4":
            search_histoy()    
        elif user_choice == "5":
            clear_screen()
            break
        else:
            print("Invalid Choice")

# TODO: Need to make this recent history feature. 
# ! Not Completed
def search_histoy():
    # n , history = get_pokemon_by_name()
    for h in history:
        print(h)
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

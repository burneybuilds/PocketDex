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
def output(): 
    while True: 
        response = get_pokemon()
        if response == "Exit": 
            clear_screen() 
            break
        elif response == "Data Not Found": 
            print("No Pokemon with such name found. Please try again.") 
        elif response == "Number":
            print("Invalid Input.")
        else: # show the ouput in a nice format.
            id = response["id"]
            name = response["name"]
            height = response["height"]
            type_name = response["types"][0]["type"]["name"]
            weight = response["weight"]
            #history = search_histoy()
            clear_screen()
            cli_art()
            print("                                        ")
            print("========================================")
            print(f"| ID: {id}                             ")
            print(f"| Name: {name}                         ")    
            print(f"| Type: {type_name}                    ")
            print(f"| Height: {height}                     ")
            print(f"| Weight: {weight}                     ")
            print("========================================")
            print("                                        ")
            #print(history)

def get_pokemon():
    while True: #Runs a infinite loop until the user enters "1" to exit.
        pokemon = input("Enter the Name of the Pokemon: ").strip().title()  # Takes input and stores it in pokemon.
        if pokemon == "1":
            return "Exit"
        elif pokemon.isdigit():
            return "Number" 
        else:
            url = requests.get("https://pokeapi.co/api/v2/pokemon/")
            if url.status_code == 200: # check if the api end is working or not.
                pokemon_name = pokemon 
                request_url = "https://pokeapi.co/api/v2/pokemon/" + pokemon_name
                response = requests.get(request_url) # just for debugging
                if response.status_code ==  404:
                    return "Data Not Found"
                else:
                    pokemon_data = response.json()  # Get the data from the api in the json format.
                    return pokemon_data #Sends the json data to bridge fucntion to display the data in a nice format.


def random_pokemon():
    pokemon_id = random.randint(1, 1025)
    pokemon_id =str(pokemon_id)
    request_url = "https://pokeapi.co/api/v2/pokemon/" + pokemon_id
    response = requests.get(request_url)
    if response.status_code == 200:
        pokemon_data = response.json()
        index_id = pokemon_data["id"]
        name = pokemon_data["name"]
        height = pokemon_data["height"]
        type_name = pokemon_data["types"][0]["type"]["name"]
        weight = pokemon_data["weight"]
        clear_screen()
        cli_art()
        print("                                        ")
        print("========================================")
        print(f"| ID: {index_id}                       ")
        print(f"| Name: {name}                         ")    
        print(f"| Type: {type_name}                    ")
        print(f"| Height: {height}                     ")
        print(f"| Weight: {weight}                     ")
        print("========================================")
        print("                                        ")
    elif response.status_code == 404:
        return "Connection Time-Out."


def search_menu():
    while True: #Runs a infinite loop until the user enters "3" to exit.
        cli_art() # You can remove this if you want. 
        print("=======================")
        print("1. Search   ") 
        print("2. Random Pokemon ")
        print("3. About Me ") 
        print("3. Exit     ")
        print("=======================")
        user_choice = input("Enter your Choice: ") #Takes Input and stores it in user_choice.
        if user_choice == "1":  # Currently, 1 is string not a int and so the other.
            output()
        elif user_choice == "2":
            random_pokemon()
        elif user_choice == "3":
            about_me() 
        elif user_choice == "4":
            clear_screen()
            break
        else:
            print("Invalid Choice")

# TODO: Need to make this recent history feature. 
# ! Not Completed
def search_histoy():
    store = 5 
    for _ in store:
        history = []
        _ , name = get_pokemon()
        if name == "Exit" or name == "Number" or name == "404":
            continue
        else:
            history.append(name)
    recent_history = f"Recent: {history}"
    return recent_history

def main():
    # Clear the screen before runing the program
    clear_screen()
    search_menu()

if __name__ == "__main__":
    main()

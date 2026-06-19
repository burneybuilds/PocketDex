import requests
import os 


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


def output(): # This function takes the response from the API and displays it in a nice format.
    while True: #Runs a infinite loop until the user enters "1" to exit.
        response = get_pokemon() # takes the output from the fuction get pokemon and stores it in response.
        if response == "Exit": # checks if it is exit then break the fucntion and return to the main menu.
            break
        else: # or show the ouput in a nice format.
            name = response["name"]
            height = response["height"]
            type_name = response["types"][0]["type"]["name"]
            weight = response["weight"]
            clear_screen()
            print("                                        ")
            print("========================================")
            print(f"Name: {name}")
            print(f"Type: {type_name}")
            print(f"Height: {height}")
            print(f"Weight: {weight}")
            print("========================================")
            print("                                        ")#Runs a infinite loop until the user enters "1" to exit.

def get_pokemon():
    while True: #Runs a infinite loop until the user enters "1" to exit.
        pokemon = input("Enter the Name of the Pokemon: ").strip().title()  # Takes input and stores it in pokemon.
        if pokemon == "1":
            return "Exit" 
        else:
            url = requests.get("https://pokeapi.co/api/v2/pokemon/")
            if url.status_code == 200: # check if the api end is working or not.
                pokemon_name = pokemon 
                request_url = "https://pokeapi.co/api/v2/pokemon/" + pokemon_name
                response = requests.get(request_url) # just for debugging
                pokemon_data = response.json()  # Get the data from the api in the json format.
                return pokemon_data #Sends the json data to bridge fucntion to display the data in a nice format.


def search_menu():
    while True: #Runs a infinite loop until the user enters "3" to exit.
        cli_art() # You can remove this if you want. 
        print("=======================")
        print("1. Search   ") 
        print("2. About Me ") 
        print("3. Exit     ")
        print("=======================")
        user_choice = input("Enter your Choice: ") #Takes Input and stores it in user_choice.
        if user_choice == "1":  # Currently, 1 is string not a int and so the other.
            output() # Call a fucntion call Output() around line 38.
        elif user_choice == "2":
            about_me() # This is fucntion, just to let you know who made it. 
        elif user_choice == "3":
            break
        else:
            print("Invalid Choice")

def main():
    search_menu()
    # user_choice = input("Enter your Choice: ") #Takes Input and stores it in user_choice
    # if user_choice.isdigit():
    #     search_menu(user_choice)
    # else:
    #     print("Invalid Choice")

if __name__ == "__main__":
    main()


"""
Data Flow: 





"""
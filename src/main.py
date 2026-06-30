import os 
import random
import parser
import command

"""
# def cli_art():
Moved to cli_display.py
"""
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

"""
def random_info():
Moved this fucntion to Cli_display.py
"""

def clear_screen(): #This Function Clear the screen.
    os.system("cls" if os.name == "nt" else "clear") # I have no idea what it does. 


"""
# def handle_search(): 
Moved to  search to def search_menu():
"""

"""
# def get_pokemon_by_name():
Moved this function to poke_api.py 
"""

"""
# def random_pokemon_by_id():
Moved this fucntion to poke_api.py 
"""
"""
# s_history = [] # empty list 
    # s_history.append(pokemon_name)  # Future me will forget what I searched.
    # searchs = ", ".join(s_history)
    # search = " / ".join(s_historu).title # This code has been promoted to "historical artifact" status.
    #history = search_histoy()
    clear_screen()  # Every Pokédex deserves a dramatic entrance.
    # cli_art()"""

# s_history = [] # This needs to sit outside the fucntion or else it will get updated eveytime the fucntion is called.
def display_pokemon(pokemondata):
    print("                                                                              ")
    print("= General Info ===============================================================")
    print("                                                                              ")
    print(f"| ID: {pokemondata["id"]}                               ") 
    print(f"| Name: {pokemondata["name"]}                                   ")    
    print(f"| Type: {pokemondata["types"]}                              ")
    print(f"| Abilities: {pokemondata["abilities"]}                     ")
    print(f"| Height: {pokemondata["height"]}                               ")
    print(f"| Weight: {pokemondata["weight"]}                               ")
    print("|                                                                            ")
    print(f"| Status : {pokemondata["status"]}                                                         ")
    print("                                                                              ")
    print("= Stats ======================================================================")
    print("                                                                              ")
    print(f"| HP : {pokemondata["hp"]}                                     ")                                       
    print(f"| Attack : {pokemondata["attack"]}                             ")           
    print(f"| Defense : {pokemondata["defense"]}                           ")
    print(f"| Special Attack : {pokemondata["special_attack"]}          ")
    print(f"| Special Defense : {pokemondata["special_defense"]}           ")
    print("                                                                              ")
    print(f"= Discription: {pokemondata["description"]}")
    print("======================================================================")
    print("1. Press 1 to go back || 2. Press 2 to Get More Info About the Pokemon")
    print()

"""
def api_status():
Moved to Cli_display.py
"""

"""
#def layout_fucntion():
This fucntion have been moved to cli_display
"""

def search_menu():
    while True:
        keyword, pokemon_name = command.commands_input()
        if keyword == "/search":
            data = parser.parser_data(pokemon_name)
            
            if data == "Not Found":
                print("Invalid Input.")
                continue
            
            display_pokemon(data)
        elif keyword == "/random":
            pokemon_id = random.randint(1, 1025)
            data = parser.parser_data(str(pokemon_id))
            display_pokemon(data)
        elif keyword == "/clear":
            os.system("cls" if os.name == "nt" else "clear")
            continue
        elif keyword == "/exit":
            print("Bye...")
            os.system("cls" if os.name == "nt" else "clear")
            break
        elif keyword == "/help":
            info = command.help()
            for i in info:
                print(i)
        elif keyword == "/info":
            about_me()
        
     
        """Why didnt i remove this ? beacuse this was the first cli ui i made."""
        # print("=======================")
        # print("1. Search Pokemon (Name / ID)  ") 
        # print("2. Random Pokemon              ")
        # print("3. About Me                    ") 
        # print("4. Exit                        ")
        # print("=======================")
        # user_choice = input("Enter your Choice: ") #Takes Input and stores it in user_choice.
        # if user_choice == "1":  # Currently, 1 is string not a int and so the other.
        #     response, extra_data, pokemon_name = command.commands_input()
        #     display_pokemon(response, extra_data, pokemon_name)
        # elif user_choice == "2":
        #     response, extra_data, pokemon_name = poke_api.random_pokemon_by_id()
        #     display_pokemon(response, extra_data, pokemon_name)
        # elif user_choice == "3":
        #     about_me() 
        # elif user_choice == "4":
        #     clear_screen()
        #     break   
        # else:
        #     print("Invalid Choice")
        #     clear_screen()
 
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
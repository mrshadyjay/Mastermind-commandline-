#jonathanosei-ntiamoah  student number: 22139615
# this is the main file for the mastermind game



#calling pre made functions i will use later on the life of the game 

from single_playermode import single_player_mode 
from two_playermode import two_player_mode
from campaign_mode import campaign_mode_start 


def main(): 
    print("Welcome to Mastermind!!!!")
    print("1. Single Player Mode")
    print("2. Two Player Mode")
    print("3. Campaign Mode")
    print("4. Help")
    print("5. Exit")

    while True:
        user_choice = input("Please select an option (1-5): ")

        if user_choice == '1':
            single_player_mode()
        elif user_choice == '2':
            two_player_mode()
        elif user_choice == '3':
            campaign_mode_start()


#this bit here will run the help.txt file so the user can see the rules of the game
        elif user_choice == '4':

            with open("help.txt", "r", encoding="utf-8") as help_file:

                help_content = help_file.read()
                print(help_content)


        elif user_choice == '5':
            print("Goodbye!")
            break
        else:
            print(" Invalid choice. Maybe try picking from 1-5 :) .")


if __name__ == "__main__":
    main()

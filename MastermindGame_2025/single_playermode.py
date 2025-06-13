#jonathanosei-ntiamoah  student number: 22139615
# this is the single player file for the mastermind game



#updated to get the shared and determined values for single player mode from game_functions
from game_functions import generate_random_code, check_guess, colours, code_length, max_guesses


def single_player_mode():

    import main
    guesses_left = max_guesses #keeping a local copy here so it is not modified outside as i will use this in other modes

    # our colour set
    #colours = ['R', 'O', 'Y', 'G', 'B']
    # this will be the length of the code 
    #code_length = 4
    # the player wil have this amountt of guesses 
  #  max_guesses = 10

    # this will generate a random code for the player to guess 
    secret_code = generate_random_code(colours, code_length)


    print("Welcome to Single Player Mode!")
    print("Try to guess the secret code!")
    print(f"You have {guesses_left} guesses, choose wisely! :) ")


  
    while guesses_left > 0:
        print(f"Available colours: {colours}")
        player_guess = input(f"Make a guess, pick {code_length} colours from {colours}: ").upper().split()

        if len(player_guess) != code_length:
            print(f"Please enter exactly {code_length} colours.\n")
            continue

        if any(colour not in colours for colour in player_guess):
            print(f"Invalid colour detected. Please choose from {colours}.\n")
            continue

        black_pegs, white_pegs = check_guess(secret_code, player_guess)

        print(f"✓ Black peg(s): {black_pegs}, ○ White peg(s): {white_pegs}")

        if black_pegs == code_length:
            print("Congratulations! You've guessed the secret code, you are a mastermind! ;)")
            replay = input("Would you like to play again? Press 'Y' for Yes or 'N' for No to return to main menu: ").upper()
            if replay == 'Y':
                single_player_mode()
                return
            elif replay == 'N':
                main()
                return
            else:
                print("Invalid input. Press 'Y' or 'N' to either restart or go back to the main menu.")
                return

        guesses_left -= 1
        print(f"You have {guesses_left} guesses left.\n")

    print(f"Sorry, you LOSTTTTTT. The secret code was: {secret_code} Would you like to try again?")
    retry = input("Press 'Y' for Yes or 'N' for No to return to main menu: ").upper()
    if retry == 'Y':
        single_player_mode()
    elif retry == 'N':
        main()
    else:
        print("Invalid input. Press 'Y' or 'N'.")

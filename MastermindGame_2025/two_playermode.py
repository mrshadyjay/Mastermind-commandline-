#jonathanosei-ntiamoah  student number: 22139615
# this is the two player file for the mastermind game


from game_functions import check_guess, colours, code_length, max_guesses
import getpass





def two_player_mode():
    import main
    guesses_left = max_guesses  # keeping a local copy here so it is not modified outside as i will use this in other modes



#introduce them to the game first. show them the colours we have and ask for player 1's input
    print("Welcome to Mastermind's Two Player Mode!")
    print("Player 1, Remember to keep your code a secret from Player 2!")
    print(f"Pick {code_length} colours from: {colours} in any order")   

    while True:
        secret_code = getpass.getpass(f"Enter your secret code of {code_length} colours: ").upper().split()
        if len(secret_code) == code_length and all(color in colours for color in secret_code):
            print("Thank you, Player 1! The secret code has been set.")
            break
        else:
            print(f"Invalid code. Please enter exactly {code_length} colours from the available colours: {colours}")
    
    # now pass over to player 2
    print("Player 2, it's your turn to guess the code!")
    print(f"You have {guesses_left} guesses, choose wisely! :) ")


#will implement the same logic i used for single player guessing 
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
                two_player_mode()
                return
            elif replay == 'N':
                main()  
                return
            else:
                print("Invalid input. Press 'Y' or 'N'.")
                return

        guesses_left -= 1
        print(f"You have {guesses_left} guesses left.\n")

    print("Sorry, you could not beat the mastermind, YOU LOSSEEEEE")

    print(f"The secret code was: {' '.join(secret_code)}")
    
    print("Would you like to try again or take turns?")
    retry = input("Press 'Y' for Yes or 'N' for No to return to main menu: ").upper()
    if retry == 'Y':
        print ("Thank you for choosing to play again! Have fun!")
        two_player_mode()
        return
    elif retry == 'N':
        main()  
        return
    else:
        print("Invalid input. Press 'Y' or 'N'.")
        return
   

#jonathanosei-ntiamoah  student number: 22139615
# this is the campaign mode file for the mastermind game



from game_functions import check_guess, colours, code_length, generate_random_code, max_guesses


def campaign_mode_start():
    import main
    #keeping a local copy here so it is not modified outside as i will use this in other modes
    guesses_left = max_guesses  
   
    # this will be the length of the code from the start that will be 4 
    current_codelength = code_length
    available_colours = colours

  
#how many levels there will be in the game
    levelamount = 4

#welcome the user to the new level here 

    print ("Welcome to Campaign Mode!")
    print("Each level will get harder with a longer code and more colours.")

    for level in range(1, levelamount + 1):
        print(f"--- LEVEL {level} ---")

        # now the code length will increase by 1 each time
        current_codelength += 1

        if level == 2:
            available_colours += ['P']  # itll then add pink to level 2
        elif level == 3:
            available_colours += ['C']  #and then cyan to level 3
        elif level == 4:
            available_colours += ['M'] #and magenta to level 4

        guesses_left = max_guesses
        secret_code = generate_random_code(available_colours, current_codelength)
        print(f"Guess the secret code with {current_codelength} colours.")
        print(f"Available colours: {available_colours}")
        print(f"You have {guesses_left} guesses.")



        #now for the guessing while looops
        while guesses_left > 0:
            player_guess = input(f"Enter your guess (use {current_codelength} colours): ").upper().split()
            if len(player_guess) != current_codelength:
                print(f"Please enter exactly {current_codelength} colours.")
                continue
            if any(colour not in available_colours for colour in player_guess):
                print(f"Invalid colour detected. Please choose from {available_colours}.")
                continue
            black_pegs, white_pegs = check_guess(secret_code, player_guess)
            print(f"✓ Black peg(s): {black_pegs}, ○ White peg(s): {white_pegs}")
            if black_pegs == current_codelength:
                print("Congratulations! You've guessed the secret code, you are a mastermind! ;)")
                break
            guesses_left -= 1
            print(f"You have {guesses_left} guesses left.")
        else:
            print(f"Sorry, you lost. The secret code was: {secret_code}.")
            retry = input("Press 'Y' for Yes or 'N' for No to return to main menu: ").upper()
            if retry == 'Y':
                campaign_mode_start()
                return
            elif retry == 'N':
                main()
                return
            else:
                print("Invalid input. Press 'Y' or 'N' to either restart or go back to the main menu.")
                return

        print(f"Congratulations! You've completed Level {level}!")
        if level < levelamount:
            print("Would you like to continue to the next level?")
            retry = input("Press 'Y' for Yes or 'N' for No to return to main menu: ").upper()
            if retry == 'Y':
                continue
            elif retry == 'N':
                main()
                return
            else:
                print("Invalid input. Press 'Y' or 'N' to either restart or go back to the main menu.")
                return
        else:
            print("Thank you for playing Campaign Mode! See you next time!")

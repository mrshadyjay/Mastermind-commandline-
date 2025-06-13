#jonathanosei-ntiamoah  student number: 22139615
# these are the functions that will be used in all game modes



import random

# values that will be used in all game modes and will remain the same
colours = ['R', 'O', 'Y', 'G', 'B']
code_length = 4
max_guesses = 10
    
 # this function generates a random set with the fixed parameters of colour (R,O,Y,G,B) and length (4)
def generate_random_code(colours, length=4):
    # will start with an empty list of the code first 
    code = [] 
    #Then will loop through the length of the code and append a random colour from the colours list to the code
    for _ in range(length):
        code.append(random.choice(colours))
        # and then return the code
    return code


def check_guess(secret_code, player_guess):
    # this keeps track of how many colours are correct and in the correct spot
    black_pegs = 0  
    # this keeps track of how many colours are correct but in the wrong spot
    white_pegs = 0  

    #this will create temporary copies of the secret code and the players guess so that I can manipulate them without changing the original lists 
    # the original lists being the ones the players will use (not here now)
    temp_code = secret_code.copy()
    temp_guess = player_guess.copy()

    # first, itll loop through and check if any of the guessed colours are exactly right (same colour AND spot)
    for i in range(len(secret_code)):
        if temp_guess[i] == temp_code[i]:
            black_pegs += 1  #
            temp_code[i] = None
            temp_guess[i] = None

    # then, itll check if any of the guessed colours are in the code but not in the right position
    for i in range(len(temp_guess)):
        if temp_guess[i] and temp_guess[i] in temp_code:
            white_pegs += 1  
            temp_code[temp_code.index(temp_guess[i])] = None

    return black_pegs, white_pegs





   
    
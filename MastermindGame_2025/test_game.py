#jonathanosei-ntiamoah  student number: 22139615
# this is the testfile for the mastermind game



import unittest
import random
from game_functions import generate_random_code, check_guess


colours = ['R', 'O', 'Y', 'G', 'B', 'P']  #  allowed colours first

class TestGameFunctions(unittest.TestCase):
  
  # making sure the code that’s randomly made is the right length and only uses the allowed colours  


    def generate_random_code_valid(self):
        
        secret_code = generate_random_code(colours, length=4)
        self.assertEqual(len(secret_code), 4)  # should be exactly 4 colours
        for colour in secret_code:
            self.assertIn(colour, colours)  # each colour must be from the allowed list


# this will test if the function correctly checks thatt secret code == player guess


    def check_guess_exact_match(self):
       
        secret_code = ['R', 'O', 'Y', 'G']
        player_guess = ['R', 'O', 'Y', 'G']
        result = check_guess(secret_code, player_guess)
        self.assertEqual(result, (4, 0)) #4 black pegs, 0 white pegs, meaning all colours are correct and in the right position



    def check_mixed_accuracy(self):
        # Test if the function correctly identifies mixed accuracy  
        secret_code = ['R', 'O', 'Y', 'G']
        player_guess = ['Y', 'G', 'R', 'O'] 


if __name__ == '__main__':
        unittest.main()

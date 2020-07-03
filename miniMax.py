import time

class Game:
    def __init__(self): # Constructor? 
        self.initialize_game()

    def initialize_game(self):
        self.current_state = [['.', '.', '.'] # Game Board (under the covers)
                            , ['.', '.', '.']
                            , ['.', '.', '.']]
        self.player_turn = 'X' # First player is always 'X'
    
    # gets print to the terminal 
    def draw_board(self):
        for i in range(0, 3):
            for j in range(0, 3):
                print('{}|'.format(self.current_state[i][j]), end=" ") 
            print()
        print()
    
    # Checks if the move we're making is w/in bounds and 
    def is_valid(self, px, py):
        if px < 0 or px > 2 or py < 0 or py > 2: # Bounds of play
            return False
        elif self.current_state[px][py] != '.': # Player piece
            return False                        # already present!
        else:
            return True
        
    

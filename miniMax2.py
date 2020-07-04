import time
 
class Game:
    def __init__(self):
        self.initialize_game()
        
    def initialize_game(self):
        self.current_state = [['.','.','.'],
                              ['.','.','.'],
                              ['.','.','.']]
        self.player_turn = 'X' # Player goes first, AI second, always.

    def draw_board(self):
        for i in range(0, 3):
            for j in range(0, 3):
                print('{}!'.format(self.current_state[i][j]), end=" ")
            print()
        print()
        
    def is_valid(self, px, py):
        # Bounds of play
        if px < 0 or px > 2 or py < 0 or py > 2:
            return False
        # Checks destination of move to avoid over-write
        elif self.current_state[px][py] != '.':
            return False
        else: # Move valid
            return True
    
    # EVALUATION FXN, Used many times by the sim to determine which move
    # to make next
    def is_end(self):
        for i in range(0, 3): # Scans from left to right vertically
            if (self.current_state[0][i] != '.' and # 
                self.current_state[0][i] == self.current_state[1][i] and
                self.current_state[1][i] == self.current_state[2][i]):
                return self.current_state[0][i]
            
        for i in range(0, 3): # Scans each row, top to bottom
            if (self.current_state[i] == ['X', 'X', 'X']):
                return 'X'
            elif (self.current_state[i] == ['O', 'O', 'O']):
                return 'O'
        
        # Diagonal left to right, return top left 
        if (self.current_state[0][0] != '.' and
            self.current_state[0][0] == self.current_state[1][1] and
            self.current_state[0][0] == self.current_state[2][2]):
            return self.current_state[0][0]
    
        # Diagonal right to left, return top right
        if (self.current_state[0][2] != '.' and
            self.current_state[0][2] == self.current_state[1][1] and
            self.current_state[0][2] == self.current_state[2][0]):
            return self.current_state[0][2]
    
        # Full Board
        for i in range(0, 3):
            for j in range(0, 3):
                if (self.current_state[i][j] == '.'): # Continue playing
                    return None
    
        # All spaces taken, TIE
        return '.'
    
    # AI Is always trying to Max 
    def max(self):
        # Aribtrarily small value of maxv
        maxv = -2 # loss: -1, tie: 0, win +1
    
        px = None # Dest x coordinate
        py = None # Dest y coordinate
    
        result = self.is_end() # Is game over? 
    
        if result == 'X': # Human wins
            return (-1, 0, 0)
        elif result == 'O': # AI wins
            return (1, 0, 0)
        elif result == '.': # Tie
            return (0, 0, 0)
    
        # Game continues, 
        # For each space on the field that's empty, calc the best move. 
        for i in range(0, 3):
            for j in range(0, 3):
                if self.current_state[i][j] == '.':
                    self.current_state[i][j] = 'O' # AI makes a move
                    (m, min_i, min_j) = self.min() # finds best max available by minimizer
                    if m > maxv: # if there was a maximizing move:
                        maxv = m # update the maxv to the maximizing move
                        px = i # set the coordinate for maximizing move
                        py = j # set the coordinate for maximizing move
                    # Setting back the field to empty
                    self.current_state[i][j] = '.' # reset test for next move
        return (maxv, px, py) # Suggested next move to be run
    
    # Human, always trying to minimize 
    def min(self):
        # Arbitrarily high minv value
        minv = 2 # -1: win, 0: tie, 1: loss
        qx = None # dest coord
        qy = None # dest coord
    
        result = self.is_end() # check if game goes on
    
        if result == 'X': # Hooman wins
            return (-1, 0, 0)
        elif result == 'O': # AI wins
            return (1, 0, 0)
        elif result == '.': # TIE
            return (0, 0, 0)
    
        # For each available space on the board, check what the game
        # will  look like after our opponent moves
        for i in range(0, 3):
            for j in range(0, 3):
                if self.current_state[i][j] == '.': # simulate a move here
                    self.current_state[i][j] = 'X' # set for simulation
                    (m, max_i, max_j) = self.max() # check if next move is a loss or win or tie
                    if m < minv: # a minimizing choice was found
                        minv = m # suggest this destination
                        qx = i
                        qy = j
                    self.current_state[i][j] = '.' # reset
    
        return (minv, qx, qy) # return the destination
    
    def play(self):
        while True: # Infinite play
            self.draw_board()
            self.result = self.is_end() # Check if game is over
            
            # Terminal messages
            if self.result != None: # None = Game continues
                if self.result == 'X':
                    print('The winner is X!')
                elif self.result == 'O':
                    print('The winner is O!')
                elif self.result == '.':
                    print("It's a tie!")
    
                self.initialize_game() # restart
                return
    
            # Human turn
            if self.player_turn == 'X':
                while True:
                    start = time.time() # gets exec time for miniMax
                    (m, qx, qy) = self.min() # recursive
                    end = time.time() # exec time for miniMax
                    print('MiniMax Eval duration: {}s'.format(round(end - start, 7)))
                    print('Recommended: X = {}, Y = {}'.format(qx, qy))
    
                    px = int(input('Insert the X coordinate: '))
                    py = int(input('Insert the Y coordinate: '))
    
                    (qx, qy) = (px, py) # dest coordinates = input coordinates 
    
                    if self.is_valid(px, py): # checks validity of move
                        self.current_state[px][py] = 'X' # make move
                        self.player_turn = 'O' # AI's turn
                        break
                    else:
                        print('Invalid move! Try again.')
    
            # AI turn
            else:
                (m, px, py) = self.max() # run miniMax, get best move
                self.current_state[px][py] = 'O' # make best move.
                self.player_turn = 'X' # Human's turn
                
def main():
    g = Game() # Create instance of our game
    g.play() # run play method

if __name__ == "__main__":
    main() # start here.
   
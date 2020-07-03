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
    
    def is_end(self):
        for i in range(0, 3): # Vertical win
            if(self.current_state[0][i] != '.' and
                self.current_state[0][i] == self.current_state[1][i] and
                self.current_state[1][i] == self.current_state[2][i]):
                return self.current_state[0][i]

        for i in range(0, 3): # Horizontal win
            if(self.current_state[i] == ['X', 'X', 'X']):
                return 'X'
            elif(self.current_state[i] == ['O', 'O', 'O']):
                return 'O'
        
        # Diagonal left to right
        if(self.current_state[0][0] != '.' and 
            self.current_state[0][0] == self.current_state[1][1] and
            self.current_state[0][0] == self.current_state[2][2]):
            return self.current_state[0][0]
    
        # Diagonal right to left
        if(self.current_state[0][2] != '.' and 
            self.current_state[0][2] == self.current_state[1][1] and
            self.current_state[0][2] == self.current_state[2][0]):
            return self.current_state[0][2]
        
        # Is board full? 
        for i in range(0, 3):
            for j in range(0, 3):
                if(self.current_state[i][j] == '.'):
                    return None

        return '.'
        
    def max(self):
        maxv = -2
        px = None
        py = None
        
        result = self.is_end()
        
        if result == 'X':
            return (-1, 0, 0)
        elif result == 'O':
            return (1, 0, 0)
        elif result == '.':
            return (0, 0, 0)
            
        for i in range(0, 3):
            for j in range(0, 3):
                if self.current_state[i][j] == '.':
                    self.current_state[i][j] == 'O'
                    (m, min_i, min_j) = self.min()
                    
                    if m > maxv:
                        maxv = m
                        px = i
                        py = j
                        
                    self.current_state[i][j] = '.'
        return (maxv, px, py)
        
    def min(self):
        minv = 2
        qx = None
        qy = None

        result = self.is_end()

        if result == 'X':
            return (-1, 0, 0)
        elif result == 'O':
            return (1, 0, 0)
        elif result == '.':
            return (0, 0, 0)

        for i in range(0, 3):
            for j in range(0, 3):
                if self.current_state[i][j] == '.':
                    self.current_state[i][j] = 'X'
                    (m, max_i, max_j) = self.max()

                    if m < minv:
                        minv = m
                        qx = i
                        qy = j

                    self.current_state[i][j] = '.'

        return (minv, qx, qy)

    def play(self):
        while True:
            self.draw_board() # Start game
            self.result = self.is_end()

            if self.result != None:
                if self.result == 'X':
                    print('The winner is X')
                elif self.result == 'O':
                    print('The winner is O')
                elif self.result == '.':
                    print('It\'s a tie!')

                self.initialize_game()
                return

            # Player's turn
            if self.player_turn == 'X':
                while True:
                    (m, qx, qy) = self.min()
                    print('rec\'d move: x = {}, y = {}'.format(qx, qy))

                    px = int(input('Insert x coordinate: '))
                    py = int(input('Insert y coordinate: '))

                    (qx, qy) = (px, py)

                    if self.is_valid(px, py):
                        self.current_state[px][py] = 'X'
                        self.player_turn = 'O'
                        break
                    else:
                        print('The move is not valid, try again')

            else:
                (m, px, py) = self.max()
                self.current_state[px][py] = 'O'
                self.player_turn = 'X'

def main():
    g = Game()
    g.play()

if __name__ == "__main__":
    main()

# your code goes here
import string
import random
import os
import sys
import time
from IPython.display import clear_output

def ChessBoardSetup():
    # lower-case for BLACK and upper-case for WHITE
    board = [['r', 't', 'b', 'q', 'k', 'b', 't', 'r'], 
             ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
             ['.', '.', '.', '.', '.', '.', '.', '.'], 
             ['.', '.', '.', '.', '.', '.', '.', '.'],
             ['.', '.', '.', '.', '.', '.', '.', '.'],
             ['.', '.', '.', '.', '.', '.', '.', '.'],
             ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
             ['R', 'T', 'B', 'Q', 'K', 'B', 'T', 'R']]
    return board

def DrawBoard():
    for i in range(8):
        for j in range(8):
            print(board[i][j], end = " ")
        print()
    print()

def MovePiece(x, y, u, v):
    # write code to move the one chess piece
    # this function will at least take the move (from-peice and to-piece) as input and return the new board layout
    if IsMoveLegal(x, y, u, v):
        board[u][v] = board[x][y]
        board[x][y] = "."
        DrawBoard()
    else:
        print("Illegal move :P")
        
def IsMoveLegal(x, y, u, v):
  # return True if a move (from-piece and to-piece) is legal, else False
  # this is the KEY function which contains the rules for each piece type
    whitePieces = ['r', 't', 'b', 'q', 'k', 'p']
    blackPieces = ['R', 'T', 'B', 'Q', 'K', 'P']
    fromPiece = board[x][y]
    toPiece = board[u][v]

    # Check bounds
    if x < 0 or x > 7 or y < 0 or y > 7 or u < 0 or u > 7 or v < 0 or v > 7:
        print("Out of bounds!")
        return False
    # Must move
    if x == u and y == v:
        print("Invalid: Don't just stand there, do something!") 
        return False
    # Check membership of piece
    if fromPiece not in whitePieces and fromPiece not in blackPieces:
        print("Invalid: piece selection!")
        return False
    # No Team kills
    if fromPiece in whitePieces and toPiece in whitePieces:
        print("Invalid: team kill!")
        return False
    if fromPiece in blackPieces and toPiece in blackPieces:
        print("Invalid: team kill!")
        return False

    # Range utility fxn's make logic simpler
    if x < u: # going down
        srcX = x
        destX = u
    else: # going up
        srcX = u
        destX = x
    if y < v: # going right
        srcY = y
        destY = v
    else: # going left
        srcY = v
        destY = y

    if fromPiece in whitePieces: # Fighting down
        if fromPiece == 'p' and IsClearPath(srcX, srcY, destX, destY) and x < u:
            return True
        elif fromPiece == 'r' and IsClearPath(srcX, srcY, destX, destY):
            # white rook logic
            return True
        elif fromPiece == 't':
            # white knight logic
            return True
        elif fromPiece == 'b':
            # white bishop logic
            return True
        elif fromPiece == 'q':
            # white queen logic
            return True
        elif fromPiece == 'k' and IsClearPath(srcX, srcY, destX, destY):
            # white king logic
            return True
    
    elif fromPiece in blackPieces: # Fighting up
        if fromPiece == 'P':
        # white pawn logic
            return True
        elif fromPiece == 'R':
        # white rook logic
            return True
        elif fromPiece == 'T':
        # white knight logic
            return True
        elif fromPiece == 'B':
        # white bishop logic
            return True
        elif fromPiece == 'Q':
        # white queen logic
            return True
        elif fromPiece == 'K':
        # white king logic
            return True

    return False

# def GetListOfLegalMoves():


#def GetPiecesWithLegalMoves():
    # gets a list of all pieces for the current player that have legal moves 
    # a piece can be denoted just by (row, col)


#def IsCheckmate():
    # returns True if the current player is in checkmate, else False


#def IsInCheck():
    # returns True if a given player is in Check state
    # One way to check: 
    #   find given player's King
    #   check if any enemy player's piece has a legal move to the given player's King
    #   return True if there is any legal move


def IsClearPath(srcX, srcY, destX, destY):
  # helper function to figure out if a move is legal for straight-line moves (rooks, bishops, queens, pawns)
  # returns True if the path is clear for a move (from-piece and to-piece), non-inclusive
    for i in range(srcX, destX):
        for j in range(srcY, destY):
            if(board[i][j] != '.'):
                return False
            # add if statement to check if the spots on the way are empty
    return True

#def DoesMovePutPlayerInCheck():
    # makes a hypothetical move (from-piece and to-piece)
    # returns True if it puts current player into check

# TEST MAIN()
board = ChessBoardSetup()
MovePiece(1, 0, 3, 0)
MovePiece(0, 0, 5, 0)
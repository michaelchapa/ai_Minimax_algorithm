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
    if DEBUG:
        print("@ 0 1 2 3 4 5 6 7")
    for i in range(8):
        if DEBUG:
            print (i, end = " ")
        for j in range(8):
            print(board[i][j], end = " ")
        print()
    print()

def MovePiece(x, y, u, v):
    if IsMoveLegal(x, y, u, v):
        board[u][v] = board[x][y]
        board[x][y] = "."
        DrawBoard()
    else:
        print("Illegal move :P")
        
def IsMoveLegal(x, y, u, v):
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
    
    # White Pieces: (p)awn, (r)ook, knigh(t), (b)ishop, (q)ueen, (k)ing
    if fromPiece in whitePieces: 
        if fromPiece == 'p' and IsClearPath(srcX, srcY, destX, destY) and x < u:
            return True
        elif fromPiece == 'r' and IsClearPath(srcX, srcY, destX, destY) \
            and RookMoves(srcX, srcY, destX, destY):
            return True 
        elif fromPiece == 't' and (destX, destY) in KnightMoves(srcX, srcY):
            return True 
        elif fromPiece == 'b' and IsClearPath(srcX, srcY, destX, destY):
            return True 
        elif fromPiece == 'q' and IsClearPath(srcX, srcY, destX, destY):
            return True 
        elif fromPiece == 'k' and IsClearPath(srcX, srcY, destX, destY):
            return True 
    
    # Black Pieces: (P)awn, (R)ook, knigh(T), (B)ishop, (Q)ueen, (K)ing
    elif fromPiece in blackPieces: 
        if fromPiece == 'P' and IsClearPath(srcX, srcY, destX, destY) and x > u:
            return True 
        elif fromPiece == 'R' and IsClearPath(srcX, srcY, destX, destY) \
            and RookMoves(srcX, srcY, destX, destY):
            return True 
        elif fromPiece == 'T' and (destX, destY) in KnightMoves(srcX, srcY):
            return True 
        elif fromPiece == 'B' and IsClearPath(srcX, srcY, destX, destY):
            return True 
        elif fromPiece == 'Q' and IsClearPath(srcX, srcY, destX, destY):
            return True 
        elif fromPiece == 'K' and IsClearPath(srcX, srcY, destX, destY):
            return True 

    return False

# Generates all 8 Knight moves, filters all out of bounds moves
def KnightMoves(srcX, srcY): 
    possibleMoves = []
    possibleMoves.append((srcX - 2, srcY - 1))
    possibleMoves.append((srcX - 2, srcY + 1))
    possibleMoves.append((srcX + 2, srcY - 1))
    possibleMoves.append((srcX + 2, srcY + 1))
    possibleMoves.append((srcX - 1, srcY - 2))
    possibleMoves.append((srcX + 1, srcY - 2))
    possibleMoves.append((srcX - 1, srcY + 2))
    possibleMoves.append((srcX + 1, srcY + 2))
      
    # Filter out of bounds moves; x == z[0], y == z[1]
    possibleMoves = [z for z in possibleMoves if z[0] >= 0 
                     if z[0] < 8 if z[1] >= 0 if z[1] < 8]
    
    return possibleMoves

def RookMoves(srcX, srcY, destX, destY):
    if (destX - srcX) > 0 and srcY == destY:
        return True
    if (destY - srcY) > 0 and srcX == destX: 
        return True
    print("FAIL")
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
    if srcX == destX: # populate the list with one value for iteration
        rangeX = [srcX]
    else:
        rangeX = [x for x in range(srcX + 1, destX)]
    if srcY == destY: # populate the list with one value for iteration
        rangeY = [srcY]
    else:
        rangeY = [y for y in range(srcY + 1, destY)]
    
    for x in rangeX:
        for y in rangeY:
            if(board[x][y] != '.'):
                return False
    return True

#def DoesMovePutPlayerInCheck():
    # makes a hypothetical move (from-piece and to-piece)
    # returns True if it puts current player into check

# TEST MAIN()
board = ChessBoardSetup()
DEBUG = True
DrawBoard()


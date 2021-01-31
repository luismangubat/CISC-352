# Initialize board size 
def boardSize(n):
    #prepare a board
    board = [[0 for x in range(n)] for x in range(n)]
    #set initial positions
    return queenPlacement(board, 0, 0)

# Place all queen in a safe state
def queenPlacement(board, row, column):

    #base case
    if row > len(board)-1:
        yield board

    #check every column of the current row if its safe to place a queen
    while column < len(board):
        if isSafe(board, row, column):
            #place a queen
            board[row][column] = 1
            #place the next queen with an updated board
            for solution in queenPlacement(board, row+1, 0):
                yield solution
            return
        else:
            column += 1
    #there is no column that satisfies the conditions. Backtrack
    for c in range(len(board)):
        if board[row-1][c] == 1:
            #remove this queen
            board[row-1][c] = 0
            #go back to the previous row and start from the last unchecked column
            for solution in queenPlacement(board, row-1, c+1):
                yield solution

def isSafe(board, row, column):
    queens = []
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] == 1:
                queen = (r,c)
                queens.append(queen)
    for queen in queens:
        qr, qc = queen
        #check if the pos is in the same column or row
        if row == qr or column == qc:
            return False
        #check diagonals
        if (row + column) == (qr+qc) or (column-row) == (qc-qr):
            return False
    return True

import sys, pprint
sys.setrecursionlimit(10000)
for solution in boardSize(5):
    pprint.pprint(solution)
#hw10.py
import copy

###############################################
# ignore_rest
###############################################

# Place these imports in hw10.py below the ignore_rest line!

from hw10_rectangula_tester import testSolveRectangula
from hw10_rectangula_tester import playRectangula


def boardcount(board):
    (rows, cols) = (len(board), len(board[0]))
    total = 0
    for row in range(rows):
        for col in range(cols):
            if board[row][col] != 0:
                total += 1
    return total

def isLegal(row, col, widht, height, trueboard):
    for 
    pass


def solveRectangula(board, result = None, tempboard=[0], trueboard = None):
    (rows, cols) = (len(board), len(board[0]))
    if result ==None: result = []
    if boardcount(tempboard) == len(result):
        return result
    else: #not the same number of rectangles as the numbers in board 
        tempboard = copy.deepcopy(board)
        if trueboard ==None:
            trueboard = []
            for row in range(rows): trueboard += [[False]*cols]

        for possibility in range(possibilities):
            if isLegal(row, col, widht, height, trueboard):
                result.append # place the queen and hope it works
                solution = solveRectangula(col+1)
                if (solution != None):
                    # ta da! it did work
                    return solution
                queenRow[col] = -1 # pick up the wrongly-placed queen
        # shoot, can't place the queen anywhere
        return None
print(makeTrueBoard(board))
testSolveRectangula(solveRectangula)
playRectangula(solveRectangula)
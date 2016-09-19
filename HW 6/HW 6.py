# hw6.py
# Sachi Nagada, snagada, GG

#Place the Autograded solutions here

def checkDuplicity(a): # a has to be a 2D list
    (rows,cols) = (len(a), len(a[0])) 
    resultset = set()
    for row in range(rows):
        for col in range(cols):
            resultset.add(a[row][col]) #adds to set to see if unique element
    if len(resultset) == rows*cols: # 
        return True #returns True if no duplicates
    return False #False if there are duplicates

def checkSum(a):
    (rows,cols) = (len(a), len(a[0]))
    finaltotal = sum(a[0])
    for col in range(cols):
        collist = []
        for row in range(rows):
            collist.append(a[row][col]) # creates a list of column
            if sum(a[row]) != finaltotal: # checks the sum of the row
                return False
        if sum(collist) != finaltotal: # checks the sum of the column
            return False
    (diagonal1, diagonal2) = ([],[])
    for col in range(0,cols):
        diagonal1.append(a[col][col]) # checks for top left to bottom right
        diagonal2.append(a[cols-1-col][col]) # top right to bottom left
    if sum(diagonal1) != finaltotal or sum(diagonal2) != finaltotal:
        return False # Returns false if the diagonal sum is not the same
    return True 

def isMagicSquare(a):
    rows = len(a)
    if rows == 1:
        return True
    cols = len(a[0])
    if rows != cols: return False #makes sure its a square
    for row in range(rows):
        #checks for ragged 2d lists
        if len(a[row]) != cols: return False
        for col in range(cols): 
            elem = a[row][col]
            if type(elem) != int: #checks its an integer
                return False
    Duplicate = checkDuplicity(a) # looks for repeating values
    summation = checkSum(a) # checks the sum of rows,columns, diagonals
    if (Duplicate == True) and (summation == True):
        return True
    return False

def checkDuplicity2(a):
    (rows,cols) = (len(a), len(a[0])) 
    resultset = set()
    for row in range(rows):
        for col in range(cols):
            resultset.add(a[row][col]) #adds to set to see if unique element
    if 0 in resultset:
        return False # can't have 0's in King's Tour
    if len(resultset) == rows*cols: # 
        return True #returns True if no duplicates
    return False #False if there are duplicates

def isKingsTour(board):
    (rows, cols) = (len(board), len(board[0]))
    duplicate = checkDuplicity2(board) #checks for duplicates and 0's in list
    if duplicate ==False:
        return False
    #similar to wordSearch from class notes
    #http://www.cs.cmu.edu/~112/notes/notes-2d-lists-examples.html
    for row in range(rows): 
        for col in range(cols):
            num = board[row][col]
            if num!= (rows*cols): #to account for the largest number in list
                result = kingsTourFromCell(board,num,row,col)
                if result == False:
                    return False
    return True

#similar to wordSearchFromCell from class notes. Cited above
def kingsTourFromCell(board,num,startRow,startCol):
    for drow in [-1,0,1]: #goes in all directions from cell
        for dcol in [-1,0,1]:
            if drow!=0 or dcol!=0: # doesn't check the center position
                result = kingsTourInDirection(board,num,startRow,
                                            startCol,drow,dcol)
                if result == True:
                    return True
    return False

def kingsTourInDirection(board,num,startRow,startCol,drow,dcol):
    (rows,cols) = (len(board), len(board[0]))
    row = startRow + drow #checks the directions
    col = startCol + dcol
    #checks if the position on board has a number that is larger than num
    # or that the row or col is within index
    if row<0 or row>=rows or col<0 or col>=cols or board[row][col] != num+1:
        return False
    return True

def areLegalValues(values):
    N2 = len(values) #N2 represents N**2 values
    sqrt = round(N2**0.5) 
    difference = sqrt**2 - N2 #only perfect squares will have 0 difference
    if difference == 0:
        valuelist = []
        for value in values:
            if value !=0: #0s can occur multiple times
                if value in valuelist: # checks for duplicates
                    return False
                elif value not in range(N2+1): #makes sure only integers
                    return False
                else:
                    valuelist.append(value)
        return True
    return False #if not a perfect square

def isLegalRow(board, row):
    rows = len(board[0])
    if row in range(rows): #makes sure the row is between 0 and N2-1
        values = board[row]  
        result = areLegalValues(values)
        if result ==True:
            return True
    return False #if not in range or illegal values

def isLegalCol(board, col): #assumes no ragged 2D lists
    (rows,cols) = (len(board),len(board[0]))
    if col in range(cols): # makes sure it's between 0 and N2-1
        collist=[]
        for row in range(rows):
            collist.append(board[row][col]) #stores values of the column
        result = areLegalValues(collist)
        if result==True:
            return True
    return False #if not col in range or if illegal

def isLegalBlock(board, block):
    (rows,cols)=(len(board), len(board[0]))
    blockSize = round(rows**0.5) #the number of rows and cols in each block
    blockCol = block%blockSize #determines column for blocks
    blockRow = block//blockSize #determines row for blocks
    values = []
    #ranges over the rows that are part of the block row
    for row in range(blockRow*blockSize,(blockRow+1)*blockSize):
        #ranges overs the cols that are part of the block col
        for col in range(blockCol*blockSize, (blockCol+1)*blockSize):
            values.append(board[row][col])
    result = areLegalValues(values)
    return result #result will be either True or False

def isLegalSudoku(board):
    (rows,cols)=(len(board), len(board[0]))
    blocks = round(rows**0.5)
    for row in range(rows): #rows tested first to confirm N**2 2D list
        rowResult = isLegalRow(board,row)
        if rowResult == False: #even if false for a single row
            return False
    for col in range(cols): #cols tested next to confirm len(cols) is N**2
        colResult = isLegalCol(board,col)
        if colResult == False: # even if false for a single col
            return False
    for block in range(blocks):
        blockResult = isLegalBlock(board,block)
        if blockResult == False: # checks if false for every block
            return False
    return True 

######################################################################
# ignore_rest: The autograder will ignore all code below here
######################################################################

#Test Functions

def testcheckSum():
    print("Testing checkSum()...", end="")
    assert(checkSum([[2,7,6],[9,5,1],[4,3,8]])==True)
    assert(checkSum([[4,9,2],[3,5,7],[8,1,6]])==True)
    assert(checkSum([[1,2],[3,4]])==False)
    print("Passed.")

def testcheckDuplicity():
    print("Testing checkDuplicity()...",end="")
    assert(checkDuplicity([[2,2],[3,4]])==False)
    assert(checkDuplicity([[1,2],[3,4]])==True)
    assert(checkDuplicity([[1,2,3],[5,4,3]])==False)
    print("Passed.")

def testisMagicSquare():
    print("Testing isMagicSquare()...",end="")
    assert(isMagicSquare([[2,7,6],[9,5,1],[4,3,8]])==True)
    assert(isMagicSquare([[2,7,6],[9,5],[4,3,8]])==False) # ragged 2D list
    assert(isMagicSquare([[2,7,6],[9,5,6],[4,3,8]])==False) # duplicate
    print("Passed.")

def testcheckDuplicity2():
    print("Testing 2()...",end="")
    assert(checkDuplicity2([[2,0],[3,4]])==False)
    assert(checkDuplicity2([[1,2],[3,4]])==True)
    assert(checkDuplicity2([[1,2,3],[5,4,3]])==False)
    print("Passed.")

def testisKingsTour():
    print("Testing...isKingsTour()...",end="")
    assert(isKingsTour([[3,2,1],[6,4,0],[5,7,8]])==False)
    assert(isKingsTour([[3,2,1],[6,4,9],[5,7,8]])==True)
    assert(isKingsTour([[1,2,3],[7,4,8],[6,5,9]])==False)
    assert(isKingsTour([[1,14,15,16],[13,2,7,6],[12,8,3,5],[11,10,9,4]])==True)    
    print("Passed.")

def testareLegalValues():
    print("Testing...areLegalValues()", end = "")
    assert(areLegalValues([1,2,3,4,5,6])==False) #not a perfect square
    assert(areLegalValues([1,2,3,4])==True) #perfect square and no repeats
    assert(areLegalValues([1,2.2,4,5])==False) #2.2 is not an integer
    print("Passed.")

b = [[ 5, 3, 0, 0, 7, 0, 0, 0, 0],
  [ 6, 0, 0, 1, 9, 5, 0, 0 ],
  [ 0, 9, 8, 0, 0, 0, 0, 6, 0 ],
  [ 8, 0, 0, 0, 6, 0, 0, 0, 3 ],
  [ 4, 0, 0, 8, 0, 3, 0, 0, 1 ],
  [ 7, 0, 0, 0, 2, 0, 0, 0, 6 ],
  [ 0, 6, 0, 0, 0, 0, 2, 8, 0 ],
  [ 0, 0, 8, 4, 1, 9, 0, 0, 5 ],
  [ 0, 0, 8, 0, 7, 0, 0, 7, 9 ]
]

def testisLegalRow():
    print("Testing...isLegalRow()", end = "")
    assert(isLegalRow(b,1)==False) #len not n**2
    assert(isLegalRow(b,2)==True) #perfect square length and no repeats
    assert(isLegalRow(b,8)==False) # 7 repeats
    print("Passed.")

def testisLegalCol():
    print("Testing...isLegalCol()", end = "")
    assert(isLegalCol(b,1)==True) #len n**2 and no repeats
    assert(isLegalCol(b,2)==False) #8 repeats
    assert(isLegalCol(b,7)==True) # no repeats and len n**2
    print("Passed.")

def testisLegalBlock():
    print("Testing...isLegalBlock()", end = "")
    assert(isLegalBlock(b,0)==True) #no repeats
    assert(isLegalBlock(b,6)==False) #8 repeats
    assert(isLegalBlock(b,4)==True) # no repeats
    print("Passed.")

a = [
  [ 5, 3, 0, 0, 7, 0, 0, 0, 0 ],
  [ 6, 0, 0, 1, 9, 5, 0, 0, 0 ],
  [ 0, 9, 8, 0, 0, 0, 0, 6, 0 ],
  [ 8, 0, 0, 0, 6, 0, 0, 0, 3 ],
  [ 4, 0, 0, 8, 0, 3, 0, 0, 1 ],
  [ 7, 0, 0, 0, 2, 0, 0, 0, 6 ],
  [ 0, 6, 0, 0, 0, 0, 2, 8, 0 ],
  [ 0, 0, 0, 4, 1, 9, 0, 0, 5 ],
  [ 0, 0, 0, 0, 8, 0, 0, 7, 9 ]
]
c = [
  [ 5, 3, 0, 0, 7, 0, 0, 0, 0 ],
  [ 6, 0, 0, 1, 9, 5, 0, 0, 0 ],
  [ 0, 9, 8, 0, 0, 0, 0, 6, 0 ],
  [ 8, 0, 0, 0, 6, 0, 0, 0, 3 ],
  [ 4, 0, 0, 8, 0, 3, 0, 0, 1 ],
  [ 7, 0, 0, 0, 2, 0, 0, 0, 6 ],
  [ 0, 6, 0, 0, 0, 0, 2, 8, 0 ],
  [ 0, 0, 0, 4, 1, 9, 0, 0, 5 ],
  [ 0, 0, 0, 0, 8, 0, 0, 7 ]
]

def testisLegalSudoku():
    print("Testing...isLegalSudoku()", end = "")
    assert(isLegalSudoku(a)==True) #no repeats
    assert(isLegalSudoku(c)==False) # missing the last element
    assert(isLegalSudoku(b)==False) # repeats and ragged 2D list
    print("Passed.")

def testAll():
    testisMagicSquare()
    testcheckDuplicity()
    testcheckSum()
    testisKingsTour()
    testcheckDuplicity2()
    testareLegalValues()
    testisLegalRow()
    testisLegalCol()
    testisLegalBlock()
    testisLegalSudoku()

#testAll()
#Place the manually graded solutions here

from tkinter import *
import math

####################################
# Othello
####################################

#from class notes on Othello
#http://www.cs.cmu.edu/~112/notes/notes-2d-lists-examples.html#othello

def make2dList(rows, cols):
    a=[]
    for row in range(rows): a += [[0]*cols]
    return a

def playOthello(rows, cols, data):
    # create initial board
    board = make2dList(rows, cols)
    board[rows//2][cols//2] = board[rows//2-1][cols//2-1] = 1
    board[rows//2-1][cols//2] = board[rows//2][cols//2-1] = 2
    (currentPlayer, otherPlayer) = (1,2)
    # and play until the game is over
    while True:
        if (hasMove(board, currentPlayer) == False):
            if (hasMove(board, otherPlayer)):
               (currentPlayer, otherPlayer) = (otherPlayer, currentPlayer)
            else:
                break
        (row, col) = getMove(board, currentPlayer, data)
        makeMove(board, currentPlayer, row, col)
        (currentPlayer, otherPlayer) = (otherPlayer, currentPlayer)

def hasMove(board, player):
    (rows, cols) = (len(board), len(board[0]))
    for row in range(rows):
        for col in range(cols):
            if (hasMoveFromCell(board, player, row, col)):
                return True
    return False

def hasMoveFromCell(board, player, startRow, startCol):
    (rows, cols) = (len(board), len(board[0]))
    if (board[startRow][startCol] != 0):
        return False
    for dir in range(8):
        if (hasMoveFromCellInDirection(board, player, startRow, startCol, dir)):
            return True
    return False

def hasMoveFromCellInDirection(board, player, startRow, startCol, dir):
    (rows, cols) = (len(board), len(board[0]))
    dirs = [ (-1, -1), (-1, 0), (-1, +1),
             ( 0, -1),          ( 0, +1),
             (+1, -1), (+1, 0), (+1, +1) ]
    (drow,dcol) = dirs[dir]
    i = 1
    while True:
        row = startRow + i*drow
        col = startCol + i*dcol
        if ((row < 0) or (row >= rows) or (col < 0) or (col >= cols)):
            return False
        elif (board[row][col] == 0):
            # no blanks allowed in a sandwich!
            return False
        elif (board[row][col] == player):
            # we found the other side of the 'sandwich'
            break
        else:
            # we found more 'meat' in the sandwich
            i += 1
    return (i > 1)

def makeMove(board, player, startRow, startCol):
    # assumes the player has a legal move from this cell
    (rows, cols) = (len(board), len(board[0]))
    for dir in range(8):
        if (hasMoveFromCellInDirection(board, player, startRow, startCol, dir)):
            makeMoveInDirection(board, player, startRow, startCol, dir)
    board[startRow][startCol] = player

def makeMoveInDirection(board, player, startRow, startCol, dir):
    (rows, cols) = (len(board), len(board[0]))
    dirs = [ (-1, -1), (-1, 0), (-1, +1),
             ( 0, -1),          ( 0, +1),
             (+1, -1), (+1, 0), (+1, +1) ]
    (drow,dcol) = dirs[dir]
    i = 1
    while True:
        row = startRow + i*drow
        col = startCol + i*dcol
        if (board[row][col] == player):
            # we found the other side of the 'sandwich'
            break
        else:
            # we found more 'meat' in the sandwich, so flip it!
            board[row][col] = player
            i += 1

def isLegalMove(board, player, row, col):
    (rows, cols) = (len(board), len(board[0]))
    if ((row < 0) or (row >= rows) or (col < 0) or (col >= cols)): return False
    return hasMoveFromCell(board, player, row, col)

def getMove(board, player, data):
    (row, col) = data.board
    return (row,col)


def othelloInit(data):
    n = 8 # number of rows and cols
    blockSize = data.width/n
    r = blockSize/2
    data.player = "black"
    (white1Row, white1Col) = (3,3)
    (white2Row, white2Col) = (4,4)
    (black1Row, black1Col) = (3,4)
    (black2Row, black2Col) = (4,3)
    #determining the center points of the initial 4 pieces
    (white1x, white1y) = (white1Row*blockSize + r, white1Col*blockSize + r)
    (white2x, white2y) = (white2Row*blockSize + r, white2Col*blockSize + r)
    (black1x, black1y) = (black1Row*blockSize + r, black1Col*blockSize + r)
    (black2x, black2y) = (black2Row*blockSize + r, black2Col*blockSize + r) 
    data.circleCenters = [(white1x, white1y,"white"),(white2x, white2y,"white"),
    (black1x, black1y,"black"),(black2x, black2y,"black")]

    data.board = [] #will contain row and col of move

def othelloMousePressed(event, data):
    pointClicked = (event.x, event.y)
    rows = 8 #number of rows
    blockSize = data.width/rows #number of pixels for each block
    boardRow = event.y//blockSize # determines which row the piece would go
    boardCol = event.x//blockSize # determines which col the piece would go
    data.board = (boardRow, boardCol)
    board = make2dList(rows, rows)
    data.Player = "white" if (data.Player == "black") else "black"
    cx = (boardCol*blockSize + (boardCol+1)*blockSize)/2 
    cy = (boardRow*blockSize + (boardRow+1)*blockSize)/2 #center of circle
    if (cx,cy) not in data.circleCenters:
        #if isLegalMove(board, data.Player, boardRow, boardCol):
        data.circleCenters.append((cx, cy, data.Player))

def othelloKeyPressed(event, data):
    # use event.char and event.keysym
    pass

def othelloTimerFired(data):
    pass

def drawBoardhelper(canvas, height, width):
    (rows,cols) = (8,8) #number of rows in othello board
    (blockWidth, blockHeight) = (width/rows, height/rows)
    for row in range(rows):
        for col in range(cols):
            left = col*blockWidth
            right = (col+1)*blockWidth
            top = row*blockHeight
            bottom = (row+1)*blockHeight
            if (row+col)%2 == 0:
                color = "dark green"
            else:
                color = "green"
            canvas.create_rectangle(left,top,right,bottom, fill = color)


def othelloRedrawAll(canvas, data):
    n = 8 # number of rows and columns
    drawBoardhelper(canvas, data.height, data.width)
    for circleCenter in data.circleCenters:
        (cx, cy,data.Player) = circleCenter
        r = 35
        canvas.create_oval(cx-r, cy-r, cx+r, cy+r, fill=data.Player)
    if len(data.circleCenters)== n**2:
        canvas.create_text(data.width/2, data.height/2, 
        text = "Game Over", fill = "black", font = "Times 58 bold")


def runOthello(width=600, height=600):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        othelloRedrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        othelloMousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        othelloKeyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        othelloTimerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    othelloInit(data)
    # create the root and the canvas
    root = Tk()
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")
print(runOthello())


####################################
# FancyWheels
####################################

def rgbString(red, green, blue):
    return "#%02x%02x%02x" % (red, green, blue)

def makeWheel(canvas,row,col,sides,data):
    colorscale = 255/data.n
    anglediff = 2*math.pi/sides
    margin = 3 #the distance between the wheels
    blockWidth = data.width/data.n
    #determines center of block
    cx = (col*blockWidth + (col+1)*blockWidth)/2 
    cy = (row*blockWidth + (row+1)*blockWidth)/2
    # red increases with rows and need -1 for the no green on right
    (red, green) = (row*colorscale,(data.n-col-1)*colorscale) 
    color = rgbString(red, green, 0)
    vertices = []
    if sides%2 == 0: ang = -data.angle
    else: ang = +data.angle
    r = (blockWidth/2)-margin
    for side in range(sides):
        x = cx+r*math.cos(anglediff*side+ang) #gets center point in block
        y = cy+r*math.sin(anglediff*side+ang)
        vertices.append((x,y))
    for value in vertices:
        for val in vertices:
            canvas.create_line(value,val, fill = color)

def fancyWheelsRedrawAll(canvas,data):
    angle = 10
    for row in range(data.n): #goes through rows to determine the number of sides
        for col in range(data.n):
            sides = row + col + 2 + 2
            makeWheel(canvas,row,col,sides,data)

def fancyWheelsInit(data):
    data.n = 5
    data.timerDelay = 100
    data.timerCounter = 0
    data.angle = 0
    data.isPaused = False

    
def fancyWheelsMousePressed(event, data):
    pass

def fancyWheelsKeyPressed(event, data):
    if (event.keysym == "Left") or (event.keysym =="Down"):
        if data.n >1:
            data.n-=1
    if (event.keysym == "Right") or (event.keysym =="Up"):
        data.n+=1
def doStep(data):
    data.timerCounter+=1
    if (data.timerCounter % 2 == 0):
        data.angle = data.timerCounter*math.pi/18 # 10 degrees
    
def fancyWheelsTimerFired(data):
    if (not data.isPaused): doStep(data)

####################################
# run function for FancyWheels
####################################

def runFancyWheels(width=600, height=600):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        fancyWheelsRedrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        fancyWheelsMousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        fancyWheelsKeyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        fancyWheelsTimerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    fancyWheelsInit(data)
    # create the root and the canvas
    root = Tk()
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

print(runFancyWheels())

print(runFancyWheels())
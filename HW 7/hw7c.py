# hw7c.py
# Sachi Nagada + snagada + GG
#Collaborator: John Villarraga + jvillar1

from tkinter import *
import random

####################################
# customize these functions
####################################

#from 2D lists class notes
#http://www.cs.cmu.edu/~112/notes/notes-2d-lists.html

def make2dList(rows, cols):
    a=[]
    for row in range(rows): a += [["blue"]*cols]
    return a

def init(data):
    #are the same because I want square blocks
    data.colSize = (data.height-2*data.margin)//data.rows
    data.rowSize = (data.height-2*data.margin)//data.rows 
    data.board=make2dList(data.rows,data.cols)
       
    #The seven pieces
    iPiece = [
    [ True,  True,  True,  True]
    ]

    jPiece = [
    [ True, False, False ],
    [ True, True,  True]
    ]

    lPiece = [
    [ False, False, True],
    [ True,  True,  True]
    ]

    oPiece = [
    [ True, True],
    [ True, True]
    ]

    sPiece = [
    [ False, True, True],
    [ True,  True, False ]
    ]

    tPiece = [
    [ False, True, False ],
    [ True,  True, True]
    ]

    zPiece = [
    [ True,  True, False ],
    [ False, True, True]
    ]
    tetrisPieces = [ iPiece, jPiece, lPiece, oPiece, sPiece, tPiece, zPiece ]
    tetrisPieceColors = [ "red", "yellow", "magenta", "pink", "cyan", "green", 
    "orange" ]
    data.tetrisPieces = tetrisPieces 
    data.tetrisPieceColors = tetrisPieceColors
    data.color = "blue" #for the board background
    data.num = random.randint(0,6) #to determine random tetris pieces
    data.piece = data.tetrisPieces[data.num]
    data.fallingPieceRow = 0 #initial position that the pieces come from
    data.fallingPieceCol = data.cols//2 - len(data.piece[0])//2
    data.timerDelay = 500 #0.5 second
    data.isGameOver = False
    data.score = 0
    data.isPause = False

def newFallingPiece(data):
    data.num = random.randint(0,6)
    data.color = data.tetrisPieceColors[data.num] #corresponds to each piece
    data.piece = data.tetrisPieces[data.num]
    data.fallingPieceRow = 0 #initial center position for tetris pieces
    data.fallingPieceCol = data.cols//2 - len(data.piece[0])//2

def drawFallingPiece(canvas,data):
    fill = data.tetrisPieceColors[data.num]
    (rows,cols) = (len(data.piece),len(data.piece[0]))
    for row in range(rows):
        for col in range(cols):
            #only draws cell when it's true because piece exists there
            if data.piece[row][col] == True:
                drawCell(canvas, data, row+data.fallingPieceRow, 
                    col+data.fallingPieceCol, fill) 
                #add the fallingPieceRow to determine where on board

def drawBoard(canvas,data):
    for row in range(data.rows):
        for col in range(data.cols):
            fill = data.board[row][col] #board will store strings of colors
            drawCell(canvas,data,row,col,fill)
                         
def drawCell(canvas,data, row,col,fill):
    m = 1 #outline width
    # outer rectangle - outline
    canvas.create_rectangle(data.margin+(col*data.colSize), 
    data.margin+(row*data.rowSize), data.margin+(col+1)*data.colSize, 
    data.margin+(row+1)*data.rowSize, fill="black")
    #inner rectanlge
    canvas.create_rectangle(m+data.margin+(col*data.colSize), 
    m+data.margin+(row*data.rowSize), data.margin+(col+1)*data.colSize-m, 
    data.margin+(row+1)*data.rowSize-m, fill=fill) 

def moveFallingPiece(data, drow, dcol):
    data.fallingPieceRow += drow #does the move first
    data.fallingPieceCol += dcol
    legal = fallingPieceIsLegal(data)
    if fallingPieceIsLegal(data)==False: #undo the move if illegal
        data.fallingPieceRow -= drow
        data.fallingPieceCol -= dcol
    return legal #tells if te move is legal or illegal

def fallingPieceIsLegal(data):
    (rows,cols) = (len(data.piece),len(data.piece[0]))
    for row in range(rows):
        for col in range(cols):
            if data.piece[row][col] == True:
                #set boundaries for row
                if (((rows + data.fallingPieceRow) > data.rows) or 
                    (data.fallingPieceRow < 0)):
                    return False
                #set boundaries for the columns
                if (((cols + data.fallingPieceCol) > data.cols) or 
                (data.fallingPieceCol < 0)): 
                    return False
                #when another piece is there
                if (data.board[row+data.fallingPieceRow]
                    [col+data.fallingPieceCol] != "blue"):
                    return False
    return True

def rotateFallingPiece(data):
    oldPiece = data.piece #store non rotated piece
    oldFallingRow = data.fallingPieceRow
    oldFallingCol = data.fallingPieceCol
    rows,cols = len(data.piece), len(data.piece[0]) 
    newPiece = make2dList(cols,rows)
    for col in range(cols):
        for row in range(rows):
            newPiece[col][row] = oldPiece[row][col] #transpose of the oldPiece
    #switches first and last row for the final rotation step      
    newPiece[0],newPiece[-1] = newPiece[-1], newPiece[0] 
    data.piece = newPiece
    #for rotating about the center
    newRow = oldFallingRow + len(oldPiece)//2 - len(newPiece)//2
    data.fallingPieceRow = newRow
    newCol = oldFallingCol + len(oldPiece[0])//2 - len(newPiece[0])//2
    data.fallingPieceCol = newCol
    #if illegal, then goes back to original position - oldPiece
    if fallingPieceIsLegal(data) == False:
        data.piece = oldPiece
        data.fallingPieceRow = oldFallingRow
        data.fallingPieceCol = oldFallingCol

def placeFallingPiece(data):
    fill = data.tetrisPieceColors[data.num]
    (rows,cols) = (len(data.piece),len(data.piece[0]))
    for row in range(rows):
        for col in range(cols):
            if data.piece[row][col] == True:
                #makes the pieces part of the board
                (data.board[data.fallingPieceRow+row] 
                    [data.fallingPieceCol + col])= fill
    removeFullRows(data)

def removeFullRows(data):
    (rows,cols) = (len(data.board),len(data.board[0]))
    newRow = make2dList(rows,cols)
    fullRows = 0
    for oldRow in range(rows-1,0,-1):
        amount = data.board[oldRow].count("blue")
        if amount != 0:
            newRow[oldRow + fullRows] = data.board[oldRow]
        else:
            fullRows +=1 #if no "blue" then the row is full and isn't added to
            #newRow
    data.board = newRow #sets the board to newRow where full rows are removed
    data.score += fullRows**2 #for when multiples lines are removed, 
    #more points are received

def drawScore(canvas,data): #displays score in top right corner
    canvas.create_text(data.width-50,20,text = "SCORE:" + str(data.score),
     fill = "black", font = "bold")

def mousePressed(event, data):
    # use event.x and event.y
    pass

def keyPressed(event, data):
    if data.isGameOver == False and data.isPause==False: 
        if (event.keysym == "Right"): moveFallingPiece(data,0,1)
        elif (event.keysym == "Left"): moveFallingPiece(data,0,-1)
        elif (event.keysym == "Down"): moveFallingPiece(data,1,0)
        elif (event.keysym == "Up"): rotateFallingPiece(data)
        elif (event.keysym == "p"): data.isPause = True 
        elif (event.keysym == "r"):
            data.board=make2dList(data.rows,data.cols)
            data.num = random.randint(0,6)
            data.piece = data.tetrisPieces[data.num]
            data.fallingPieceRow = 0
            data.fallingPieceCol = data.cols//2 - len(data.piece[0])//2
            data.score = 0 #score is reset with the game
    elif data.isGameOver == False and data.isPause == True:
        if (event.keysym == "u"): data.isPause = False
    else:
        if(event.keysym == "r"):
            data.board=make2dList(data.rows,data.cols)
            data.isGameOver = False
            data.num = random.randint(0,6)
            data.piece = data.tetrisPieces[data.num]
            data.fallingPieceRow = 0
            data.fallingPieceCol = data.cols//2 - len(data.piece[0])//2
            data.score = 0 #score is reset with the game

def timerFired(data):
    if data.isGameOver == False and data.isPause == False:
        if moveFallingPiece(data, +1, 0) == False:
            placeFallingPiece(data) #makes part of the board
            newFallingPiece(data) #brings a new piece to drop
            if fallingPieceIsLegal(data) == False: #checks for gameover
                data.isGameOver = True
    
def redrawAll(canvas, data):
    canvas.create_rectangle(0,0, data.width,data.height, fill="orange")
    drawBoard(canvas,data)
    drawFallingPiece(canvas,data)
    drawScore(canvas,data)
    if data.isGameOver == True:
        canvas.create_rectangle(0,0,data.width, data.height, fill = "black")
        canvas.create_text(data.width/2,data.height*1/3, 
            text = "GAME OVER", fill = "white", font="Times 30 bold")
        canvas.create_text(data.width/2,data.height*2/3, 
            text = "press 'r' to reset", fill = "white", font="Times 18 bold")
    canvas.create_text(100,350, text = "Press 'p' to pause and 'u' to unpause")

####################################
# use the run function as-is
####################################

def run(width, height,rows, cols,margin):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    data.rows = rows 
    data.cols = cols 
    data.margin = margin
    init(data)
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

def playTetris():
    rows = 15
    cols = 10
    margin = 30
    size = 20 #20 pixels is size of block
    run(margin*2 + cols*size, margin*2 + rows*size, rows, cols, margin) 

print(playTetris())
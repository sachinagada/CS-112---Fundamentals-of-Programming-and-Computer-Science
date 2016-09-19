# hw7s.py
# Sachi Nagada, snagada, GG

#started with Barebones timer, mouse, and keyboard events (events-example0.py)
from tkinter import *

####################################
# customize these functions
####################################

#from 2D lists class notes
#http://www.cs.cmu.edu/~112/notes/notes-2d-lists.html

def make2dList(rows, cols):
    a=[]
    for row in range(rows): a += [["None"]*cols]
    return a

def init(data):
    data.board = make2dList(data.rows,data.cols)
    data.points = [ ] #stores the mouse click data
    data.bounds = [ ] #converts mouse click data into rows & cols
    data.player = "green"
    data.square = [ ] # stores the top horizontal line of square
    data.squareColor = [ ] #stores data.square and the color inside
    data.color = [ ] #stores just the color of inside squares for score
    data.greenScore = 0
    data.orangeScore = 0
    data.isGameOver = False

def drawBoard(canvas,data): #creates the dots on the board
    for row in range(data.rows):
        for col in range(data.cols):
            canvas.create_oval(data.margin+col*data.blockSize,
                data.margin+row*data.blockSize,
                 data.margin+col*data.blockSize+4, 
                 data.margin+row*data.blockSize+4, fill = "black")

def getPlayer(data): #changes the color according to the player
    if data.player == "green":
        data.player = "orange"
    else:
        data.player = "green"

def getBounds(data,point): #converts the mouse click data to rows and cols
    (x,y) = point
    col = round((x-data.margin)/data.blockSize)
    row = round((y-data.margin)/data.blockSize)
    return(row,col)

def getMove(data):
    if len(data.points) > 0 and (len(data.points)%2 == 0): #need two points
        (row1,col1) = getBounds(data,data.points[0]) #rows&cols of first click
        (row2,col2) = getBounds(data,data.points[1]) #rows&cols of 2nd click
        if isLegalMove(data,row1,col1,row2,col2): 
            data.bounds.append((min(row1,row2),min(col1,col2),max(row1,row2),
                max(col1,col2),data.player))
            getPlayer(data)
        data.points = [] #resets the mouse click points to empty list. 
        #This is necessary to figure out if the next move is legal

def isLegalMove(data,row1,col1,row2,col2):
    #if the line already exists, then choosing that line is illegal move
    if (((min(row1,row2),min(col1,col2),max(row1,row2), max(col1,col2),"green") 
        in data.bounds) or 
        ((min(row1,row2),min(col1,col2),max(row1,row2), max(col1,col2),"orange") 
        in data.bounds)): 
        return False
    #each square can only be one block long
    elif (abs(row2 - row1) + abs(col2-col1)) != 1:
        return False
    else:
        return True

def checkSide1(bound1, bound2): #checks for left vertical line of square
    (row1, col1, row2, col2, color) = bound1
    (row12, col12, row22, col22, color2) = bound2
    if (row1 == row12 and col1 == col12 and row22 == row1 + 1 and col22 ==col1):
        return True
    else:
        return False

def checkSide2(bound1, bound2): #checks for bottom horizontal line of square
    (row1, col1, row2, col2, color) = bound1
    (row12, col12, row22, col22, color2) = bound2
    if (row2 == row12 and col2 == col12 and row22 == row2 and col22 ==col1+1):
        return True
    else:
        return False

#checks the right vertical line of square
def checkSide3(bound1,bound2, bound3): 
    (row1, col1, row2, col2, color) = bound1
    (row12, col12, row22, col22, color2) = bound2
    (row13, col13, row23, col23, color3) = bound3
    if (row2 == row13 and col2 == col13 and row23 == row22 and col22 ==col23):
        return True
    else:
        return False

def checkSquare(data): #checks to see if a square is made on the board
    if len(data.bounds) > 2+1:
        for i in range(len(data.bounds)):
            a = data.bounds[i]
            for j in range(len(data.bounds)):
                b = data.bounds[j]
                if a != b and checkSide1(a,b): #helper function above
                    for k in range(len(data.bounds)):
                        c = data.bounds[k]
                        if (a != b and a != c and b !=c and checkSide2(b,c)):
                            for m in range(len(data.bounds)):
                                d = data.bounds[m]
                                if (a != b and a != c and a != d and
                                 b != c and b != d and c != d):
                                    if checkSide3(a,c,d) == True:
                                        if a not in data.square:
                                    #stores the top horizontal line
                                            data.square.append(a)
                                    #stores top line and the color of player
                                            data.squareColor.append((a[0:2],
                                                data.bounds[-1][4]))
                                    # just stores the color for scoring
                                            data.color.append((data.bounds
                                                [-1][4]))
                                            data.orangeScore = (data.color.count
                                                ("orange"))
                                            data.greenScore = (data.color.count
                                                ("green"))
                                            return True                                                
    return False

def checkGameOver(data): 
    #the number of lines haves to be (19+19)x4 for 20x20 board
    if len(data.bounds)== ((data.cols-1)+(data.rows-1))*4:
        data.isGameOver = True

def drawGameOver(canvas,data): #writes messsage when game over
    if data.isGameOver == True:
        canvas.create_text(data.width/2, data.height/2, 
            text = "GAME OVER", font = "Times 40 bold", fill = "black")

def drawMoves(canvas,data): #draws the lines that each player creates
    getMove(data)
    for i in range(len(data.bounds)):
        (row1,col1,row2,col2,fill) = data.bounds[i]
        canvas.create_line(col1*data.blockSize + data.margin,
                row1*data.blockSize + data.margin,
                col2*data.blockSize + data.margin,
                row2*data.blockSize + data.margin, fill = fill)

#writes the inital of player inside the square
def drawSquare(canvas,data): 
    if checkSquare(data) == True:
        for square in range(len(data.squareColor)):
            ((row,col),color) = data.squareColor[square]
            #initials correspond to the player
            if color == "green":
                canvas.create_text((col+1)*data.blockSize,
                 (row+1)*data.blockSize, text = "G")
            else:
                canvas.create_text((col+1)*data.blockSize, 
                    (row+1)*data.blockSize, text = "O")

def drawPlayer(canvas,data): #displays whose turn it is
    canvas.create_text(data.width/2,data.height-data.margin,
        text = "Player: " + data.player)

def drawScore(canvas,data): #displays the score in bottom left corner
    canvas.create_text(data.width/10, data.height-data.margin, 
        text = "Green: " + str(data.greenScore) + "    " + "Orange: " 
        + str(data.orangeScore))

def mousePressed(event, data):
    data.points.append((event.x, event.y))

def keyPressed(event, data):
    # use event.char and event.keysym
    pass

def timerFired(data):
    pass

def redrawAll(canvas, data):
    drawBoard(canvas,data)
    drawPlayer(canvas, data)
    drawMoves(canvas,data)
    drawSquare(canvas, data)
    drawScore(canvas,data)

####################################
# use the run function as-is
####################################

def run(width, height, rows, cols, maxSecondsPerTurn, margin, size):
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
    data.rows = rows
    data.cols = cols
    data.margin = margin
    data.blockSize = size
    data.maxSecondsPerTurn = maxSecondsPerTurn
    data.timerDelay = 7000 # milliseconds
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


def playDotsAndBoxes(rows, cols, maxSecondsPerTurn):
    margin = 10
    size = 30
    run(2*margin+size*rows, 2*margin+size*cols, rows, cols, maxSecondsPerTurn,
        margin, size)

print(playDotsAndBoxes(20,20,1))
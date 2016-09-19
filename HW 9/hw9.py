# hw9.py
# Sachi Nagada + snagada + 1,GG
# Number 5 collaborated with Hardik Singh (hardiks1)

import os
from tkinter import *
import math

def findLarger(t1, t2): #compares two files and returns the larger one
    #print(t1)
    (file1, size1) = t1
    (file2, size2) = t2
    if size2 > size1:
        return (file2, size2)
    else:
        return (file1, size1)

def findLargestFileHelper(path, largest = "", largestSize = -10, d= dict()):
    #base case when it's a file
    if (os.path.isdir(path) == False):
        #dictionary has the the path and it's size so compare and return larger
        if path in d:
            (largest, largestSize) = findLarger((path, d[path]), 
                (largest, largestSize))
       #store in dictionary if not in there after getting size
        else: 
            size = os.path.getsize(path)
            d[path] = size
            (largest, largestSize) = findLarger((path, d[path]), 
                                                        (largest, largestSize))
        return (largest, largestSize)
    #recursive case when it's a folder
    else:
        for filename in os.listdir(path):
            possible =findLargestFileHelper(path + "/" + filename, 
                                                    largest, largestSize, d)
            #compares the largest file so far with the possible larger file
            (largest, largestSize) = findLarger(possible, (largest, 
                                                                largestSize))
    return (largest, largestSize)

def findLargestFile(path):
    #calls helper function above and only returns the file and not size
    (largest,largestSize) = findLargestFileHelper(path)
    return largest


def flatten(L,aux=None):
    if type(L) != list: #not a list so return the values
        return L
    else:
        if aux ==None: aux = [] #to prevent from mutating every time
        for element in L:
            if type(element) == list: #if list, then go through again
                flatten(element,aux)
            else:
                aux.append(element) #not a list so append the values to aux
    return aux

# from course notes on loops
# http://www.cs.cmu.edu/~112/notes/notes-loops.html#isPrime
def fasterIsPrime(n):
    if (n < 2):
        return False
    if (n == 2):
        return True
    if (n % 2 == 0):
        return False
    maxFactor = round(n**0.5)
    for factor in range(3,maxFactor+1,2):
        if (n % factor == 0):
            return False
    return True

def isRTP(n):
    if n<10:
        return fasterIsPrime(n)
    else:
        if fasterIsPrime(n): 
        #checks to see if each truncated value is prime
            return isRTP(n//10)
        else: #not a prime number at this point so not RTP
            return False

def findRTP(digits, n=1):
    #print(n)
    #number has the right amount of digits and is RTP
    dig = math.floor(math.log(n)/math.log(10))+1
    if dig==digits and isRTP(n):
        return n
    #doesn't have the right number of digits or isn't RTP
    else:
        for i in range(1,10):
            n += i
            if isRTP(n):
                if dig == digits: #number of digits are the same and n is RTP
                    solution = findRTP(digits, n)
                    if solution != None:
                        return solution
                else: #not the same number of digits so multiply by 10
                    solution = findRTP(digits, n*10)
                    if solution != None:
                        return solution
            #solution is none so subtract i and go through the for loop
            n -=i
        #went through the whole list and couln't find solution
        return None


# Collaborated with Hardik Singh during recitation
def getCourse(courseCatalog, courseNumber):
    if courseNumber in courseCatalog: #if in the same directory
        return courseCatalog[0] + "."+ courseNumber
    else: # has a list under the directory
        for element in courseCatalog:
            if type(element) == list: #recursive call until no more lists
                if getCourse(element, courseNumber) != None:
                    return courseCatalog[0] + "." + getCourse(element, 
                                                                courseNumber)
    return None


######################################################################
# ignore_rest: The autograder will ignore all code below here
######################################################################

def init(data):
    data.level = 0

def keyPressed(event, data):
    if (event.keysym in ["Up", "Right"]):
        data.level += 1
    elif ((event.keysym in ["Down", "Left"]) and (data.level > 0)):
        data.level -= 1

def drawHFractal(canvas, x, y, h, w, level):
    #(x,y) represents the center of the H
    # h and w represent the height and width of the H
    if (level == 0):
        canvas.create_line(x-w/2, y, x+w/2, y)
        canvas.create_line(x-w/2, y-h/2, x-w/2, y+h/2)
        canvas.create_line(x+w/2, y-h/2, x+w/2, y+h/2)
    else:
        drawHFractal(canvas, x-w/2, y-h/2, h/2, w/2, level-1)
        drawHFractal(canvas, x-w/2, y+h/2, h/2, w/2, level-1)
        drawHFractal(canvas, x+w/2, y-h/2, h/2, w/2, level-1)
        drawHFractal(canvas, x+w/2, y+h/2, h/2, w/2, level-1)


def redrawAll(canvas, data):
    for level in range(data.level+1):
        drawHFractal(canvas, data.width/2, data.height/2, 
                                           data.width/2, data.height/2, level)

    canvas.create_text(250, 25,
                       text = "Level %d H-Fractal" % (data.level),
                       font = "Arial 24 bold")

def timerFired(data): pass

def mousePressed(event, data): pass



####################################
# use the run function as-is
####################################

def run(width=500, height=500):
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
    data.margin = 20
    data.timerDelay = 100 # milliseconds
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

run()

def testfindLargestFile():
    print("Testing findLargestFile...",end = "")
    assert(findLargestFile("sampleFiles/folderA") ==
                       "sampleFiles/folderA/folderC/giftwrap.txt")
    assert(findLargestFile("sampleFiles/folderB") ==
                       "sampleFiles/folderB/folderH/driving.txt")
    assert(findLargestFile("sampleFiles/folderB/folderF") == "")
    print("Passed.")

def testfindLargestFileHelper():
    print("Testing findLargestFileHelper...", end="")
    assert(findLargestFileHelper("sampleFiles/folderA")==
        ("sampleFiles/folderA/folderC/giftwrap.txt",188))
    assert(findLargestFileHelper("sampleFiles/folderB")==
        ("sampleFiles/folderB/folderH/driving.txt",185))
    assert(findLargestFileHelper("sampleFiles/folderB/folderF")==
        ("",-10))
    print("Passed.")

def testflatten():
    print("Tetsing flatten...", end ="")
    assert(flatten([1,[2]]) == [1,2])
    assert(flatten([1,2,[3,[4,5],6],7]) == [1,2,3,4,5,6,7])
    assert(flatten(['wow', [2,[[]]], [True]]) == ['wow', 2, True])
    assert(flatten([]) == [])
    assert(flatten([[]]) == [])
    assert(flatten(3) == 3) #not a list!
    print("Passed.")

courseCatalog = ["CMU",
                    ["CIT",
                        [ "ECE", "18-100", "18-202", "18-213" ],
                        [ "BME", "42-101", "42-201" ],
                    ],
                    ["SCS",
                        [ "CS", 
                          ["Intro", "15-110", "15-112" ],
                          "15-122", "15-150", "15-213"
                        ],
                    ],
                    "99-307", "99-308"
                ]

def testgetCourse():
    print("Testing getCourse...", end = "")
    assert(getCourse(courseCatalog, "18-100") == "CMU.CIT.ECE.18-100")
    assert(getCourse(courseCatalog, "15-112") == "CMU.SCS.CS.Intro.15-112")
    assert(getCourse(courseCatalog, "15-213") == "CMU.SCS.CS.15-213")
    assert(getCourse(courseCatalog, "99-307") == "CMU.99-307")
    assert(getCourse(courseCatalog, "15-251") == None)
    print("Passed.")

def testisRTP():
    print("Testing isRTP...",end = "")
    assert(isRTP(1)==False)
    assert(isRTP(23)==True)
    assert(isRTP(233)==True)
    print("Passed.")

def testfindRTP():
    print("Testing findRTP...", end = "")
    assert(findRTP(1)==2)
    assert(findRTP(2)==23)
    assert(findRTP(3)==233)
    assert(findRTP(8)==23399339)
    print("Passed.")



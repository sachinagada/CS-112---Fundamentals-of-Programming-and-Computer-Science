# hw4.py
# Sachi Nagada + snagada + 1,GG

import math
import string
from tkinter import *
import copy

def lookAndSay(a):
    result = []
    count = 0
    for i in range(len(a)):
        count +=1
        #only appends if the numbers are not consecutive and i is not the last
        # index because trouble with i+1
        if (i+1) < len(a) and (a[i] != a[i+1]): 
            result.append((count,a[i])) 
            count = 0
        #for the case when i is the last index, breaks into two cases: if the 
        # number is consecutive or not
        elif (i == len(a)-1):
            if (a[i] != a[i-1]): #when last index is not consecutive
                result.append((1,a[i]))
            elif (a[i] == a[i-1]): # when last index is consecutive
                result.append((count,a[i]))
    return result

def inverseLookAndSay(a):
    result =[]
    for tupl in a:
        repeat = tupl[0] # the first value is the count
        value = tupl[1] # the second value is the digit repeating
        result += [value]*repeat 
    return result

def puzzleinSolution(puzzle,solution): #determines if characters in puzzle are
# in the solution
    for character in puzzle:
        if character.isalpha(): #need isalpha for the + and = signs
            if character not in solution:
                return False
    return True

def solvesCryptarithm(puzzle, solution):
    puzzle = puzzle.upper() 
    solution = solution.upper()
    if puzzleinSolution(puzzle,solution): #uses the helper function above
        result = []
        for letter in puzzle:
        #if the letter is an alphabet, the index of letter in solution is added
            if letter.isalpha():
                index = solution.index(letter)
                #converts to string so can join it later
                result.append("%d" %index) 
            #if the letter is a character (+,=), then just add the character
            elif letter.isalpha() ==False:
                result.append(letter)
        plus = result.index("+") 
        equal = result.index("=")
        #segregates the 1st line with the + and joins so it's all one number
        first = "".join(result[:plus])
        #segregates the 2nd line with + and = 
        second = "".join(result[(plus+1):equal]) 
        #the remainder of message after = is one number
        total = "".join(result[(equal+1):])
        # converts the strings to integers to see if they add up
        if (int(first) + int(second)) == int(total):
            return True
    return False

def bestScrabbleScore(dictionary,letterScores,hand):
    bestScore = 0
    bestWord = []
    lowercase = string.ascii_lowercase
    for word in dictionary: 
        letters = list(word) #converts the string to list with all the letters
        totalScore = 0
        hand2 = copy.copy(hand) 
        for letter in letters:
            if letter in hand2: #makes sure the letters from word are in hand
                index = lowercase.find(letter)
                score = letterScores[index]
                totalScore += score #adds the score that corresponds with letter
                hand2.remove(letter)
            else:
                # if the letter isn't in hand, move on to next word and lower
                # total score
                totalScore = -100 
                break
        if totalScore>bestScore: # updates the best score and best word
            bestScore = totalScore 
            bestWord = [word]
        elif bestScore == totalScore: # updates if more than one best score
            bestWord += [word]
    if bestWord == []: #if no words in the dictionary match the hand tiles
        return None
    elif len(bestWord) == 1:
        return (bestWord[0], bestScore)
    return (bestWord, bestScore)

def drawCirclePattern(n):
    height = 400 #specifies the pixels to match the 10x10 drawing on hw
    width = 400
    #similar to the runDrawing function notes
    root = Tk() 
    canvas = Canvas(root, width=width, height=height)
    canvas.pack()
    drawCirclerPatternHelper(canvas, width, height, n) #helper function below
    root.mainloop()
    print("bye!")

def drawCirclerPatternHelper(canvas, width, height,n):
    #makes sure the image fits if dimensions change
    diameter = min(width,height)/n  
    for col in range(n):
        for row in range(n):
            left = diameter*col #determines the points of the square
            top = diameter*row
            right = diameter + diameter*col
            bottom = diameter + diameter*row
            #determines the color of the circle according to the conditions
            if (row + col)%4 ==0: 
                color = "red"
            elif row%3 ==0:
                color = "green"
            elif col%2 ==1:
                color = "yellow"
            else:
                color = "blue"
            drawBullseye(canvas,left,top,right,bottom,color) # helper function

def drawBullseye(canvas,left,top,right,bottom,color):
    cx = left + (right-left)/2 # shifts the x center to the center of square
    cy = top + (bottom-top)/2 # shifts the y center to the center of the square
    radius = (right-left)/2 # radius will be half of square length
    while (radius>1):
        newleft = cx - radius #adjusts the points as the radius changes
        newtop = cy - radius
        newright = cx + radius
        newbottom = cy + radius
        canvas.create_oval(newleft, newtop, newright, newbottom, fill=color)
        radius = radius*(2/3) # changes the radius to be 2/3 of previous radius

def keepWanted(program):
    result = ""
    for line in program.splitlines():
        if line.startswith("color") or line.startswith("move"):
            if "#" in line:
                index = line.find("#") 
                line = line[:index] # removes comments from programs
            result += line + " " # adds a space to split into lists after
        elif line.startswith("left") or line.startswith("right"):
            if "#" in line:
                index = line.find("#") 
                line = line[:index] # removes comments from programs
            result += line + " " # adds a space to split into lists after
        result2 = result.split(" ")
    return result2

def runSimpleTortoiseProgram(program, winWidth=500, winHeight=500):
    #similar to the runDrawing function notes
    root = Tk() 
    canvas = Canvas(root, width=winWidth, height=winHeight)
    canvas.pack()
    program2 = keepWanted(program) #only keeps the needed the words and numbers
    #calls the helper function below
    runSimpleTortoiseProgramHelper(canvas, program2, winWidth, winHeight)
    root.mainloop()
    print("bye!")

def runSimpleTortoiseProgramHelper(canvas, program2, winWidth, winHeight):
    cx = winWidth/2 # determines the center position
    cy = winHeight/2 
    currentx = cx # where the tortoise starts
    currenty = cy
    angle = 0 # initial angle is 0 since it starts moving right
    for i in range(len(program2)):
        if program2[i] == "color": # determines the fill color
            color = program2[i+1]
            continue
        elif program2[i] == "left":
            # gets added because it goes clockwise
            angle += int(program2[i+1])*math.pi/180 # converts to radians
            continue
        elif program2[i] == "right":
            # right is being subtracted because it goes anti clockwise
            angle -= int(program2[i+1])*math.pi/180 # converts to radians
            continue
        elif program2[i] == "move":
            r = int(program2[i+1]) # the number of moves acts like a radius
            # the final x position will be the current position + movement
            # the movement will be defined by the r*cos(x) for x direction
            xend = currentx + r*math.cos(angle) 
            # the movement will be r*sin(x) for the y direction
            yend = currenty - r*math.sin(angle)
            if color != "none": # only draws line if there's color
                canvas.create_line(currentx, currenty, xend, yend, 
                    fill = color, width = 4)
            currentx = xend #updates the current x and y position
            currenty = yend

######################################################################
# ignore_rest: The autograder will ignore all code below here
######################################################################

def testlookAndSay():
    print("Testing lookAndSay()...",end ="")
    assert(lookAndSay([]) == [])
    assert(lookAndSay([1,1,1]) == [(3,1)])
    assert(lookAndSay([-1,2,7]) == [(1,-1),(1,2),(1,7)])
    assert(lookAndSay([1,1,2,3,3,2]) ==[(2, 1), (1, 2), (2, 3), (1, 2)])
    print("Passed.")

def testinverseLookAndSay():
    print("Testing inverseLookAndSay()...",end ="")
    assert(inverseLookAndSay([]) == [])
    assert(inverseLookAndSay([(3,1)]) == [1,1,1])
    assert(inverseLookAndSay([(1,-1),(1,2),(1,7)]) == [-1,2,7])
    assert(inverseLookAndSay([ (2, 1), (1, 2), (2, 3), (1, 2)]) == [1,1,2,3,3,2])
    print("Passed.")

def testpuzzleinSolution():
    print("Testing puzzleinSolution()...",end ="")
    assert(puzzleinSolution("SEND+MORE=MONEY","OMY--ENDRS") == True)
    assert(puzzleinSolution("caret","tarec") == True)
    assert(puzzleinSolution("hippopotamus","hip") == False)
    print("Passed.")

def testsolvesCryptarithm():
    print("Testing solvesCryptarithm()...",end ="")
    assert(solvesCryptarithm("SEND+MORE=MONEY","OMY--ENDRS")==True)
    assert(solvesCryptarithm("hat+cat=cts","hatcs")==True)
    assert(solvesCryptarithm("hat+cat=cts","hatsc")== False)
    print("Passed.")

dictionary =["hat","bat","cat"]
hand1 = ["b","c","a","t"]
hand2 = ["b","c","a","t","h"]
letterScores = [
#  a, b, c, d, e, f, g, h, i, j, k, l, m
  1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3,
#  n, o, p, q, r, s, t, u, v, w, x, y, z
  1, 1, 3,10, 1, 1, 1, 1, 4, 4, 8, 4,10 
]

def testbestScrabbleScore():
    print("Testing bestScrabbleScore ()...",end="")
    assert(bestScrabbleScore(dictionary,letterScores,["a","t"])==None)
    assert(bestScrabbleScore(dictionary,letterScores,hand1)==(['bat','cat'],5))
    assert(bestScrabbleScore(dictionary,letterScores,hand2)==('hat',6))
    print("Passed.")

program1 = """
move 90
right 90 # testing
left 90"""

program2 = """
color blue
# random line
right 89"""

def testkeepWanted():
    print("Testing keepWanted()...", end ="")
    assert(keepWanted(program1)== ['move', '90', 'right', '90', '',
     'left', '90', ''])
    assert(keepWanted(program2)==['color', 'blue', 'right', '89', ''])
    print("Passed.")

def testAll():
    testlookAndSay()
    testinverseLookAndSay()
    testpuzzleinSolution()
    testsolvesCryptarithm()
    testbestScrabbleScore()
    testkeepWanted()
testAll()

# if __name__ == "__main__":
   # testAll()


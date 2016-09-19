import math
import string
from tkinter import *
import copy

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

program = """
# Y
color red
right 45
move 50
right 45
move 50
right 180
move 50
right 45
move 50
color none # space
right 45
move 25

# E
color green
right 90
move 85
left 90
move 50
right 180
move 50
right 90
move 42
right 90
move 50
right 180
move 50
right 90
move 43
right 90
move 50  # space
color none
move 25

# S
color blue
move 50
left 180
move 50
left 90
move 43
left 90
move 50
right 90
move 42
right 90
move 50
"""

print(runSimpleTortoiseProgram(program, winWidth=500, winHeight=500))
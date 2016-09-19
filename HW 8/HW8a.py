# hw8a.py
# Sachi Nagada + snagada + 1,GG


from tkinter import *

####################################
# customize these functions
####################################

class Gate(object):
    def __init__(self, gateType, x, y):
        self.x = x
        self.y = y
        self.gateType = gateType
        self.inputValues = None
        self.outputValue = None
        self.inputGates = list()
        self.outputGates = list()

    def determineOutput(self):
        if self.gateType == "input" or self.gateType == "output":
            for key in self.inputValues: #same as the input
                if self.inputValues[key]==True:
                    self.outputValue = True
                else:
                    self.outputValue = False

        elif self.gateType == "not": #opposite if what the input is
            for key in self.inputValues:
                if self.inputValues[key]==True:
                    self.outputValue = False
                else:
                    self.outputValue = True
        
        elif self.gateType == "and":
            if self.inputValues == None or len(self.inputValues) < 2:
                self.outputValue = None
            elif len(self.inputValues)==2: # has two inputs now
            # got a way to get a list of values of dictionary from this website
            # http://www.tutorialspoint.com/python/python_dictionary.htm
                value = self.inputValues.values()
                if False in value: self.outputValue = False
                else: self.outputValue = True

        elif self.gateType == "or":
            if self.inputValues == None or len(self.inputValues) < 2:
                self.outputValue = None
            elif len(self.inputValues)==2: # has two inputs now
            # got a way to get a list of values of dictionary from this website
            # http://www.tutorialspoint.com/python/python_dictionary.htm
                value = self.inputValues.values()
                if True in value: self.outputValue = True
                else: self.outputValue = False


    def connectTo(self,other):
        self.outputGates.append(other)
        other.inputGates.append(self)
        
    def getInputGates(self):
        return self.inputGates

    def getMaxInputGates(self):
        return len(self.inputGates)

    def getOutputGates(self):
        return self.outputGates

    def changeOutput(self):
        #will keep on going until the output gate is empty list
        # output gates will only be for those that are not connected or outputs
        for outputGate in self.outputGates:
            if outputGate.inputValues == None:
                d = dict()
                d[self] = self.outputValue
                outputGate.inputValues = d
            #(outputGate).determineOutput()
            else:
                outputGate.inputValues[self] = self.outputValue
            (outputGate).determineOutput()
            outputGate.changeOutput()

    def setInputValue(self, value1, value2):
        if self.inputValues ==None:
            d = dict()
            d[value1]= value2
            self.inputValues = d
            self.determineOutput()
            self.changeOutput()
        else:
            self.inputValues[value1] = value2
            self.determineOutput()
            self.changeOutput()

#from OOP class notes
#http://www.cs.cmu.edu/~112/notes/notes-oop-part1.html
    def containsPoint(self, x, y):
        margin = 40
        d = ((self.x - x)**2 + (self.y - y)**2)**0.5
        return (d <= margin)

    def drawNotGate(self, canvas):
        cx = self.x
        cy = self.y
        offset = 20
        rad = 2 #radius of circle
        point1 = (cx+offset,cy)
        point2 = (cx-offset,cy-offset/2)
        point3 = (cx-offset,cy+offset/2)
        point4 = (cx+offset-rad, cy-rad)
        point5 = (cx+offset+rad, cy+rad)
        canvas.create_polygon(point1,point2,point3, fill = "black")
        canvas.create_oval(point4,point5, fill = "black")

    def drawOrGate(self, canvas):
        cx = self.x
        cy = self.y
        offset = 20
        point1 = (cx-offset, cy-offset)
        point2 = (cx, cy-offset)
        point3 = (cx+offset, cy)
        point4 = (cx, cy+offset)
        point5 = (cx-offset, cy+offset)
        point6 = (cx-offset/2, cy)
        canvas.create_polygon(point1,point2,point3,point4,point5,point6, 
                                                                fill = "black")
    def drawAndGate(self, canvas):
        cx = self.x
        cy = self.y
        offset = 20
        canvas.create_rectangle(cx-offset, cy-offset, cx + offset, cy+offset, 
                                                                fill = "black")
        canvas.create_oval(cx, cy-offset,cx + 2*offset, cy+offset, 
                                                                fill = "black")

    def drawInput(self, canvas, fill="purple"):
        cx = self.x
        cy = self.y
        rad = 10
        canvas.create_oval(cx-rad/2, cy-rad/2, cx+rad/2, cy+rad/2, fill = fill)

    def drawOutput(self, canvas, fill="green"):
        cx = self.x
        cy = self.y
        rad = 10
        canvas.create_oval(cx-rad/2, cy-rad/2, cx+rad/2, cy+rad/2, fill = fill)

    def drawGates(self, canvas):
        if self.gateType == "input":
            if self.outputValue == True:
                self.drawInput(canvas, fill = "red")
            else:
                self.drawInput(canvas)
        elif self.gateType == "output":
            if self.outputValue == True:
                self.drawOutput(canvas, fill = "red")
            else:
                self.drawOutput(canvas)
        elif self.gateType == "not":
            self.drawNotGate(canvas)
        elif self.gateType== "or":
            self.drawOrGate(canvas)
        elif self.gateType == "and":
            self.drawAndGate(canvas)


######################################################################
# ignore_rest: The autograder will ignore all code below here
######################################################################


def init(data):
    data.isPowerOn = False
    length = 60
    width = data.width/4
    height = 20
    data.clearButton = (width, height, width+length, 2*height)
    data.loadButton = (2*width, height, 2*width+length, 2*height)
    data.saveButton = (3*width, height, 3*width+length, 2*height)
    data.type=None
    offset = data.height/12
    width2 = data.width/7
    height2 = data.height/6
    data.notGateButton = (0,height2-offset, width2, 2*height2-offset)
    data.orGateButton = (0, 2*height2-offset, width2, 3*height2-offset)
    data.andGateButton = (0, 3*height2-offset, width2, 4*height2-offset)
    data.inputButton = (0, 4*height2-offset, width2, 5*height2-offset)
    data.outputButton = (0, 5*height2-offset, width2, 6*height2-offset)
    #with the initial gates shown on the buttons
    data.gatesInitial = [Gate("not", width2/2, 1.5*height2 - offset),
                  Gate("or", width2/2, 2.5*height2 - offset),
                  Gate("and", width2/2, 3.5*height2 - offset),
                  Gate("input", width2/2, 4.5*height2 - offset),
                  Gate("output", width2/2, 5.5*height2 - offset)]
    data.gates = []
    data.connection = []

# similar to bounds intersect from class notes on animation
#www.cs.cmu.edu/~112/notes/notes-animations-examples.html#sideScrollerDemo
def clickedClear(data,x,y):
    (ax0, ay0, ax1, ay1) = data.clearButton #bounds of clear button
    (bx0, by0, bx1, by1)= (x,y, x+1, y+1) #made the click into rectangle
    return ((ax1 >= bx0) and (bx1 >= ax0) and
            (ay1 >= by0) and (by1 >= ay0)) 

def clickedLoad(data,x,y):
    (ax0, ay0, ax1, ay1) = data.loadButton #bounds of Load button
    (bx0, by0, bx1, by1)= (x,y, x+1, y+1) #made the click into rectangle
    return ((ax1 >= bx0) and (bx1 >= ax0) and
            (ay1 >= by0) and (by1 >= ay0)) 

def clickedSave(data,x,y):
    (ax0, ay0, ax1, ay1) = data.saveButton #bounds of Save button
    (bx0, by0, bx1, by1)= (x,y, x+1, y+1) #made the click into rectangle
    return ((ax1 >= bx0) and (bx1 >= ax0) and
            (ay1 >= by0) and (by1 >= ay0)) 

def clickedNotGate(data, x, y):
    (ax0, ay0, ax1, ay1) = data.notGateButton #bounds of Not Gate button
    (bx0, by0, bx1, by1)= (x,y, x+1, y+1) #made the click into rectangle
    return ((ax1 >= bx0) and (bx1 >= ax0) and
            (ay1 >= by0) and (by1 >= ay0)) 

def clickedOrGate(data, x, y):
    (ax0, ay0, ax1, ay1) = data.orGateButton #bounds of Or Gate button
    (bx0, by0, bx1, by1)= (x,y, x+1, y+1) #made the click into rectangle
    return ((ax1 >= bx0) and (bx1 >= ax0) and
            (ay1 >= by0) and (by1 >= ay0)) 

def clickedAndGate(data, x, y):
    (ax0, ay0, ax1, ay1) = data.andGateButton #bounds of And Gate button
    (bx0, by0, bx1, by1)= (x,y, x+1, y+1) #made the click into rectangle
    return ((ax1 >= bx0) and (bx1 >= ax0) and
            (ay1 >= by0) and (by1 >= ay0)) 


def clickedInput(data, x, y):
    (ax0, ay0, ax1, ay1) = data.inputButton #bounds of Input button
    (bx0, by0, bx1, by1)= (x,y, x+1, y+1) #made the click into rectangle
    return ((ax1 >= bx0) and (bx1 >= ax0) and
            (ay1 >= by0) and (by1 >= ay0)) 

def clickedOutput(data, x, y):
    (ax0, ay0, ax1, ay1) = data.outputButton #bounds of Output button
    (bx0, by0, bx1, by1)= (x,y, x+1, y+1) #made the click into rectangle
    return ((ax1 >= bx0) and (bx1 >= ax0) and
            (ay1 >= by0) and (by1 >= ay0)) 

def clickedPower(data, x, y): #determines if the power button was clicked
    offset = 30
    powerRadius = 21 #radius of the button
    powerx = data.width/2
    powery = 11*data.height/12 + offset
    d = ((powerx - x)**2 + (powery - y)**2)**0.5
    return d <= powerRadius

def makeConnections(data):
    if len(data.connection)%2 == 0:
        for i in range(0,len(data.connection),2):
            gate1 = data.connection[i]
            gate2 = data.connection[i+1]
            gate1.connectTo(gate2)

# from the notes on string
# http://www.cs.cmu.edu/~112/notes/notes-strings.html#basicFileIO
def readFile(path):
    with open(path, "rt") as f:
        return f.read()

def writeFile(path, contents):
    with open(path, "wt") as f:
        f.write(contents)

def mousePressed(event, data):
    if clickedPower(data, event.x, event.y):
        data.isPowerOn = not data.isPowerOn
    if clickedClear(data, event.x, event.y):
        data.gates = []
        data.connection = []
    if clickedSave(data, event.x, event.y):
        contentsToWrite = str(data)
        writeFile("foo.py", contentsToWrite)
    if clickedLoad(data, event.x, event.y):
        contentsRead = readFile("foo.py")
    #cannont manipulate connections w/ power on for safety concerns
    if data.isPowerOn == False: 
        for gate in data.gates:
            if gate.containsPoint(event.x, event.y):
                (data.connection).append(gate)
                makeConnections(data)
        if data.type == None: 
            #check to see what button is being clicked on/gate being chosen
            if clickedNotGate(data, event.x, event.y):
                data.type = "not"
            elif clickedOrGate(data, event.x, event.y):
                data.type = "or"
            elif clickedAndGate(data, event.x, event.y):
                data.type = "and"
            elif clickedInput(data, event.x, event.y):
                data.type = "input"
            elif clickedOutput(data, event.x, event.y):
                data.type = "output"
        # the gate type is already selected and now gate is being placed
        else:
            (data.gates).append(Gate(data.type, event.x, event.y))
            data.type = None
    #power is on
    else:
        for gate in data.gates:
            #can only change power of the input values that are already on
            # the canvas
            if (gate.containsPoint(event.x, event.y) and 
                gate.gateType == "input"):
                #turn on power if no power
                if gate.inputValues == None:
                    gate.setInputValue(None, True)
                #turn off power if power is on
                elif gate.inputValues == { None:True}:
                    gate.setInputValue(None, False)
                #turn on power if power is false
                elif gate.inputValues == { None:False}:
                    gate.setInputValue(None, True)

def keyPressed(event, data):
    # use event.char and event.keysym
    pass

def timerFired(data):
    pass

def drawConnection(canvas, data):
    if len(data.connection)%2 == 0:
        for i in range(0,len(data.connection),2):
            gate1 = data.connection[i]
            gate2 = data.connection[i+1]
            if gate1.outputValue == True: fill = "red"
            else: fill = "black"
            canvas.create_line(gate1.x, gate1.y, gate2.x, gate2.y, fill = fill, 
                                                                    width = 2)
    else:
        for i in range(0,len(data.connection)-1,2):
            gate1 = data.connection[i]
            gate2 = data.connection[i+1]
            if gate1.outputValue == True: fill = "red"
            else: fill = "black"
            canvas.create_line(gate1.x, gate1.y, gate2.x, gate2.y, fill = fill,
                                                                    width = 2)

def drawPower(canvas, data):
    if data.isPowerOn == False: fill = "white"
    else: fill = "red"
    off = 21
    offset=30
    width = data.width/2
    height = 11*data.height/12 + offset
    canvas.create_oval(width-off, height-off, width+off, height+off, fill = fill)
    canvas.create_text(width, height, text = "POWER")

def drawOtherButtons(canvas,data):
    #draws clear Button
    (x1,y1,x2,y2) = data.clearButton
    canvas.create_rectangle(x1,y1,x2,y2)
    canvas.create_text((x1+x2)/2, (y1+y2)/2,text = "Clear")
    #draws load button
    (x3,y3,x4,y4) = data.loadButton
    canvas.create_rectangle(x3,y3,x4,y4)
    canvas.create_text((x3+x4)/2, (y3+y4)/2, text = "Load")
    #draws Save button
    (x5,y5,x6,y6) = data.saveButton
    canvas.create_rectangle(x5,y5,x6,y6)
    canvas.create_text((x5+x6)/2, (y5+y6)/2, text = "Save")


def drawButtons(canvas,data): #only draws the buttons on the left side 
    width = data.width/7
    height = data.height/6
    offset = data.height/12
    textOffset = 10
    buttonNames = ["NOT Gate", "OR Gate", "AND Gate", "Input", "Output"]
    for i in range(1,6):
        #creates the buttons on the left
        canvas.create_rectangle(0,(height*i) - offset, width, 
                                                        height*(i+1)-offset)
        #labels with button name
        canvas.create_text(width/2, height*(i+1)-offset-textOffset, 
                                                        text = buttonNames[i-1])
    #top line above which clear, load, and save are located
    canvas.create_line(0,offset, data.width, offset)
    #bottom line below which power is located
    canvas.create_line(0, data.height-offset, data.width, data.height-offset)

def redrawAll(canvas, data):
    drawButtons(canvas, data)
    drawPower(canvas,data)
    drawOtherButtons(canvas,data)
    drawConnection(canvas,data)
    for gate in data.gatesInitial:
        gate.drawGates(canvas)
    for gate in data.gates:
        gate.drawGates(canvas)
    
####################################
# use the run function as-is
####################################

def run(width=800, height=600):
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


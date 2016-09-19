# hw3.py
# Sachi Nagada + snagada + 1,GG

import string
import math

def newMessage(message):   # helper function that removes whitespaces
    newmessage = ""
    for c in message:
        if c not in string.whitespace:
            newmessage += c 
    return newmessage

def patternedMessage(message,pattern):
    newmessage = newMessage(message) #uses helper function above
    result = ""
    count = 0            #counter used to insert correct message character later
    for c in pattern:
        if c in string.whitespace: #the whitespaces are kept in the pattern
            result += c
        elif c not in string.whitespace: #the non whitespaces are relaced
            result += newmessage[(count%len(newmessage))] 
            count +=1
    if result.startswith("\n"):  #removes leading newline 
        result = result.replace("\n","",1)
    if result.endswith("\n"): #removes trialing newline
        result = result[:(len(result)-1)]
    return result

def encodeRightLeftCipher(message, rows):
    columns = math.ceil(len(message)/rows)
    revlowercase = string.ascii_lowercase[::-1] 
    missingcharacters = rows*columns - len(message)
    finalmessage = message + revlowercase[:missingcharacters]  #fills in missing characters
    result = ""
    for i in range(1,rows+1):
        if (i%2 == 1):   # odd rows are read from left to right
            result += finalmessage[(i-1):len(finalmessage):rows]
        elif (i%2 == 0):   # even rows are read right to left
            result += finalmessage[(len(finalmessage)-(rows+1-i)):0:-rows]
    return str(rows) + result #inserts the number in front of the message

def rowDetermine(s): #extracts the number in front of the message
    row = ""
    for c in s:
        if c.isdigit():
            row +=c
    rows = int(row)
    return rows

def messageDetermine(s): # removes the number in front of the message
    message = ""
    for c in s:
        if c.isalpha():
            message += c
    return message

def decodeRightLeftCipher(encodedMessage):
    rows = rowDetermine(encodedMessage)
    message = messageDetermine(encodedMessage)  #use helper functions above
    columns = len(message)//rows
    result = ""
    for i in range(rows):
        if (i%2==0):
            result += message[(i*columns): ((i+1)*columns)] # keeps even rows the same
        elif (i%2 ==1):
            result += message[((i+1)*columns-1):((i*columns)-1):-1] #reverses odd rows
    decode = ""
    for i in range(columns):
        decode += result[i:len(result):columns]
    initialmessage = ""
    for c in decode:
        if c in string.ascii_uppercase:  # removes the filler lowercase alphabets
            initialmessage += c
    return initialmessage

def shortGradebook(gradebook):  #helper function to condense the gradebook
    newgradebook =""
    for line in gradebook.splitlines():  
        if (line.startswith("#")) or (line.startswith("string.whitespace")):
            newgradebook += ""   #removes lines that are blank or start with #
        elif ((line.startswith("#") == False)):
            newgradebook += line + "\n"
    return newgradebook

def bestStudentAndAvg(gradebook):
    newgradebook = shortGradebook(gradebook)
    bestaverage = -1000  # not 0 becaues the average could be 0
    beststudent = ""
    for line in newgradebook.splitlines():
        if "," in line:  # ignores blank lines from the triple quotes
            total = count = 0
            name = ""
            for data in line.split(","): 
                if data.isalpha():
                    name += data
                elif str(abs(int(data))).isdigit():   #compares if the entry is name or score
                    total += int(data)
                    count += 1
            average = total/count
            if average > bestaverage:  
                bestaverage = round(average)
                beststudent = name
    return beststudent + ":" + str(bestaverage) #returns the requested format

def topLevelFunctionNames(code):
    result =""
    code = code.replace("\'","\"")
    for line in code.splitlines():
        count2 = line.count("\"")
        if (count2%2 ==1) and (line.startswith("def ")==False):
            result += ","  #inserts commas when odd number of quotes and # after quotes
        elif line.startswith("def "):
            end = line.find("(")
            functionname = line[4:end]
            if functionname not in result:  #makes sure the function isn't getting repeated
                result += functionname + "."  
            if count2%2 ==1:
               result += ","  #inserts commas when odd number of quotes and # after quotes
    commas = result.count(",")
    while (commas>0):   #the while loop is removing the functions that are in triple quote strings
        start = result.find(",")
        result = result.replace(",","",1) 
        end = result.find(",")
        result = result[:start] + result[(end+1):]
        commas -= 2
    result = result[:(len(result)-1)]
    return(result)


######################################################################
# ignore_rest: The autograder will ignore all code below here
######################################################################

s1 = """
    *     *     *
   ***   ***   ***
  ***** ***** *****
   ***   ***   ***
    *     *     *"""
s2 ="""    T     h     r
   eeD   iam   ond
  s!Thr eeDia monds
   !Th   ree   Dia
    m     o     n"""
    
def testpatternedMessage():
    print("Testing testpatternedMessage()...", end="")
    assert(patternedMessage("Sasha Fierce","*******  ******") == "SashaFi  erceSa")
    assert(patternedMessage("Go PatriOTS!", "** ** ** ** ** **") == "Go Pa tr iO TS !G")
    assert(patternedMessage("Three Diamonds!", s1) == s2)
    print("Passed.")

def testencodeRightLeftCipher():
    print("Testing encodeRightLeftCipher()...", end="")
    assert(encodeRightLeftCipher("WEATTACKATDAWN",3) == "3WTCTWNDKTEAAAAz")
    assert(encodeRightLeftCipher("WEATTACKATDAWN",4) == "4WTAWNTAEACDzyAKT")
    assert(encodeRightLeftCipher("WEATTACKATDAWN",1) == "1WEATTACKATDAWN")
    print("Passed.")

def testdecodeRightLeftCipher():
    print("Testing decodeRightLeftCipher()...", end="")
    assert(decodeRightLeftCipher("3WTCTWNDKTEAAAAz") == "WEATTACKATDAWN")
    assert(decodeRightLeftCipher("4WTAWNTAEACDzyAKT") == "WEATTACKATDAWN")
    assert(decodeRightLeftCipher("1WEATTACKATDAWN") == "WEATTACKATDAWN")
    print("Passed.")

gradebooktest1 = """
# ignore  blank lines and lines starting  with  #'s
wilma,91,93
fred,80,85,90,95,100
betty,88
"""

gradebooktest2 = """
# ignore  blank lines and lines starting  with  #'s

sasha,100
wilma,91,93
fred,80,85,90,95,100
betty,88
"""

gradebooktest3 = """
# ignore  blank lines and lines starting  with  #'s
# Testing

# testing some more
sasha,100
wilma,91,93
fred,80,85,90,95,100
# random test
betty,88
"""

def testbestStudentAndAvg():
    print("Testing bestStudentAndAvg() ...", end="")
    assert(bestStudentAndAvg(gradebooktest1)== "wilma:92")
    assert(bestStudentAndAvg(gradebooktest2)=="sasha:100")
    assert(bestStudentAndAvg(gradebooktest3)=="sasha:100")
    print("Passed.")

function1 = """def Have a great day(x) \"\"\" \ndef f(x) = x + 42 \"\"\" """
function2 = """\
def f(x): return x+42
def g(x): return x+f(x)
def f(x): return x-42
"""
function3 = '''\
def f(): return """
def g(): pass"""
'''
def testtopLevelFunctionNames():
    print("Testing topLevelFunctionNames()...", end="")
    assert(topLevelFunctionNames(function1) == "Have a great day")
    assert(topLevelFunctionNames(function2) == "f.g")
    assert(topLevelFunctionNames(function3) == "f")
    print("Passed.")

def testAll():
    testpatternedMessage()
    testencodeRightLeftCipher()
    testdecodeRightLeftCipher()
    testbestStudentAndAvg()
    testtopLevelFunctionNames()
testAll()

# if __name__ == "__main__":
   # testAll()


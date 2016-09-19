# hw1.py
# Sachi Nagada + snagada + 1,GG

import math

def almostEqual(d1, d2):
    epsilon = 10**-8
    return (abs(d2 - d1) < epsilon)

def nearestBusStop(street):
    y = math.floor(street/8) # determines closest and lowest multiple of 8
    diff = street - 8*y      # difference between the street and the multiple of 8
    if (diff > 4):              # looks at the difference to determine the closest busstop
        return(8*(y+1))
    else:
        return(8*y)

def setKthDigit(n, k, d):
    y = n - ((n//(10**k))%10)*(10**k) + d*(10**k)
    return y

def cosineZerosCount(r):
    if (r<0):             #r has to be greater than or equal to 0 (0<=x<=r)
        return 0
    else:
        return round(r / math.pi)  

def riverCruiseUpstreamTime(totalTime, totalDistance, riverCurrent):
    distance = totalDistance/2  #the one way distance
    speedofboat = (2*distance + math.sqrt((2*distance)**2 + 4*(totalTime**2)*riverCurrent**2) )/(2*totalTime) #in the water
    return distance/(speedofboat-riverCurrent) #takes into account the river current

def rectanglesOverlap(left1, top1, width1, height1, left2, top2, width2, height2):
    x1 = left1 + width1
    y1 = top1 + height1
    x2 = left2 + width2
    y2 = top2 + height2
    if (left1<=left2<=x1 or left1<=x2<=x1):   # the x points of the second are within the first rectangle
        if (top1<=top2<=y1 or top1<=y2<=y1):  # if the y points of the second are within the first rectangle
            return True
        elif(top2 <= top1 <= y2 or top2 <= y1 <= y2):  # if the y points of the first are within the second rectangle
            return True
        else:
            return False
    elif (left2 <= left1 <= x2 or left2 <= x1 <= x2):  # the x points of the first are within the second rectangle
        if (top1<=top2<=y1 or top1<=y2<=y1):           # if the y points of the second are within the first rectangle
            return True
        elif(top2 <= top1 <= y2 or top2 <= y1 <= y2):  # if the y points of the first are within the second rectangle
            return True
        else:
            return False
    else:
        return False

def rectanglesOverlap2(left1, top1, width1, height1, left2, top2, width2, height2):
    x1 = left1 + width1
    y1 = top1 + height1
    x2 = left2 + width2
    y2 = top2 + height2
    if (left1<=left2<=x1 or left1<=x2<=x1 or left2<= left1<= x2):   # the x points of the second are within the first rectangle
        if (top1<=top2<=y1 or top1<=y2<=y1 or top2<=top1<= y2):  # if the y points of the second are within the first rectangle
            return True
        else:
            return False
    else:
        return False

def lineIntersection(m1, b1, m2, b2):
    if (m1==m2):
        return None
    else:
        return (b2 - b1)/(m1 - m2)

def distance(x1, y1, x2, y2):
    return ((x2-x1)**2 + (y2-y1)**2)**0.5

def triangleArea(s1, s2, s3):
    s = (s1 + s2 + s3)/2
    return math.sqrt(s*(s-s1)*(s-s2)*(s-s3))

def threeLinesArea(m1, b1, m2, b2, m3, b3):
    x1 = lineIntersection(m1, b1, m2, b2)
    x2 = lineIntersection(m2, b2, m3, b3)
    x3 = lineIntersection(m1, b1, m3, b3)
    if (x1 == None or x2 == None or x3 == None):
        return 0
    else:
        y1 = m1*x1 + b1
        y2 = m2*x2 + b2
        y3 = m3*x3 + b3
        s1 = distance(x1, y1, x2, y2)
        s2 = distance(x1, y1, x3, y3)
        s3 = distance(x2, y2, x3, y3)
        return triangleArea(s1, s2, s3)

######################################################################
# ignore_rest: The autograder will ignore all code below here
######################################################################

def testNearestBusStop():
    print("Testing nearestBusStop()...", end="")
    assert(nearestBusStop(0) == 0)
    assert(nearestBusStop(4) == 0)
    assert(nearestBusStop(5) == 8)
    assert(nearestBusStop(12) == 8)
    assert(nearestBusStop(13) == 16)
    assert(nearestBusStop(20) == 16)
    assert(nearestBusStop(21) == 24)
    print("Passed. (Add more tests to be more sure!)")

def testSetKthDigit():
    print("Testing setKthDigit()...", end="")
    assert(setKthDigit(468, 0, 1) == 461)
    assert(setKthDigit(468, 1, 1) == 418)
    assert(setKthDigit(468, 2, 1) == 168)
    assert(setKthDigit(468, 3, 1) == 1468)
    print("Passed. (Add more tests to be more sure!)")

def testCosineZerosCount():
    print("Testing cosineZerosCount()...", end="")
    assert(type(cosineZerosCount(0)) == int)
    assert(cosineZerosCount(0) == 0)
    assert(cosineZerosCount(math.pi/2 - 0.0001) == 0)
    assert(cosineZerosCount(math.pi/2 + 0.0001) == 1)
    assert(cosineZerosCount(3*math.pi/2 - 0.0001) == 1)
    assert(cosineZerosCount(3*math.pi/2 + 0.0001) == 2)
    assert(cosineZerosCount(5*math.pi/2 - 0.0001) == 2)
    assert(cosineZerosCount(5*math.pi/2 + 0.0001) == 3)
    assert(cosineZerosCount(-math.pi/2 - 0.0001) == 0)
    assert(cosineZerosCount(-math.pi/2 + 0.0001) == 0)
    print("Passed. (Add more tests to be more sure!)")

def testRiverCruiseUpstreamTime():
    print("Testing riverCruiseUpstreamTime()...", end="")
    # example from the source notes:
    totalTime = 3 # hours
    totalDistance = 30 # 15km up, 15km back down
    riverCurrent = 2 # km/hour
    assert(almostEqual(riverCruiseUpstreamTime(totalTime,
                                               totalDistance,
                                               riverCurrent),
                       1.7888736053508778)) # 1.79 in notes
    # another simple example
    totalTime = 3 # hours
    totalDistance = 30 # 15km up, 15km back down
    riverCurrent = 0 # km/hour
    assert(almostEqual(riverCruiseUpstreamTime(totalTime,
                                               totalDistance,
                                               riverCurrent),
                       1.5))
    print("Passed. (Add more tests to be more sure!)")

def testRectanglesOverlap():
    print("Testing rectanglesOverlap()...", end="")
    assert(type(rectanglesOverlap(1, 1, 2, 2, 2, 2, 2, 2)) == bool)
    assert(rectanglesOverlap(1, 1, 2, 2, 2, 2, 2, 2) == True)
    assert(rectanglesOverlap(1, 1, 2, 2, -2, -2, 6, 6) == True)
    assert(rectanglesOverlap(1, 1, 2, 2, 3, 3, 1, 1) == True)
    assert(rectanglesOverlap(1, 1, 2, 2, 3.1, 3, 1, 1) == False)
    assert(rectanglesOverlap(1, 1, 1, 1, 1.9, -1, 0.2, 1.9) == False)
    assert(rectanglesOverlap(1, 1, 1, 1, 1.9, -1, 0.2, 2) == True)
    print("Passed. (Add more tests to be more sure!)")

def testLineIntersection():
    print("Testing lineIntersection()...", end="")
    assert(lineIntersection(2.5, 3, 2.5, 11) == None)
    assert(lineIntersection(25, 3, 25, 11) == None)
    # y=3x-5 and y=x+5 intersect at (5,10)
    assert(almostEqual(lineIntersection(3,-5,1,5), 5))
    # y=10x and y=-4x+35 intersect at (2.5,25)
    assert(almostEqual(lineIntersection(10,0,-4,35), 2.5))
    print("Passed. (Add more tests to be more sure!)")

def testDistance():
    print("Testing distance()...", end="")
    assert(almostEqual(distance(0, 0, 1, 1), 2**0.5))
    assert(almostEqual(distance(3, 3, -3, -3), 6*2**0.5))
    assert(almostEqual(distance(20, 20, 23, 24), 5))
    print("Passed. (Add more tests to be more sure!)")

def testTriangleArea():
    print("Testing triangleArea()...", end="")
    assert(almostEqual(triangleArea(3,4,5), 6))
    assert(almostEqual(triangleArea(2**0.5, 1, 1), 0.5))
    assert(almostEqual(triangleArea(2**0.5, 2**0.5, 2), 1))
    print("Passed. (Add more tests to be more sure!)")

def testThreeLinesArea():
    print("Testing threeLinesArea()...", end="")
    assert(almostEqual(threeLinesArea(1, 2, 3, 4, 5, 6), 0))
    assert(almostEqual(threeLinesArea(0, 7, 1, 0, -1, 2), 36))
    assert(almostEqual(threeLinesArea(0, 3, -.5, -5, 1, 3), 42.66666666666))
    assert(almostEqual(threeLinesArea(1, -5, 0, -2, 2, 2), 25))
    assert(almostEqual(threeLinesArea(0, -9.75, -6, 2.25, 1, -4.75), 21))
    print("Passed. (Add more tests to be more sure!)")

def getCubicCoeffs(k, root1, root2, root3):
    # Given roots e,f,g and vertical scale k, we can find
    # the coefficients a,b,c,d as such:
    # k(x-e)(x-f)(x-g) =
    # k(x-e)(x^2 - (f+g)x + fg)
    # kx^3 - k(e+f+g)x^2 + k(ef+fg+eg)x - kefg
    e,f,g = root1, root2, root3
    return k, -k*(e+f+g), k*(e*f+f*g+e*g), -k*e*f*g

def testFindIntRootsOfCubicCase(k, z1, z2, z3):
    a,b,c,d = getCubicCoeffs(k, z1, z2, z3)
    observed = findIntRootsOfCubic(a,b,c,d)
    actual = tuple(sorted([z1,z2,z3]))
    assert(observed == actual)

def testBonusFindIntRootsOfCubic():
    # only test the bonus if they tried it...
    if ("findIntRootsOfCubic" not in globals()): return
    print("Testing findIntRootsOfCubic()...", end="")
    testFindIntRootsOfCubicCase(5, 1, 3,  2)
    testFindIntRootsOfCubicCase(2, 5, 33, 7)
    testFindIntRootsOfCubicCase(-18, 24, 3, -8)
    testFindIntRootsOfCubicCase(1, 2, 3, 4)
    print("Passed. (Add more tests to be more sure!)")
 
def testAll():
    testNearestBusStop()
    testSetKthDigit()
    testCosineZerosCount()
    testRiverCruiseUpstreamTime()
    testRectanglesOverlap()
    testLineIntersection()
    testDistance()
    testTriangleArea()
    testThreeLinesArea()
    testBonusFindIntRootsOfCubic()
 
if __name__ == "__main__":
    testAll()
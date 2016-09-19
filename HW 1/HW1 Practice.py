import math

def isLegalTriangle(s1, s2, s3):
    if (s1<0 or s2<0 or s3<0):
        return False
    else:
        if (s1+s2>s3 and s1+s3>s2 and s2+s3>s1):
            return True
        else:
            return False

def testIsLegalTriangle():
    print("Testing isLegalTriangle()...", end="")
    assert(isLegalTriangle(3, 4, 5))
    assert(isLegalTriangle(5, 4, 3))
    assert(isLegalTriangle(3, 5, 4))
    assert(isLegalTriangle(0.3, 0.4, 0.5))
    assert(not isLegalTriangle(3, 4, 7))
    assert(not isLegalTriangle(7, 4, 3))
    assert(not isLegalTriangle(0, 0, 0))
    assert(not isLegalTriangle(5, -3, 1))
    assert(not isLegalTriangle(-3, -4, -5))
    print("Passed.")

testIsLegalTriangle()

def nthFibonacci(n):
    fibonacci = ((1+math.sqrt(5))**(n+1) - (1-math.sqrt(5))**(n+1))/(2**(n+1)*math.sqrt(5))
    return round(fibonacci)

def testNthFibonacci():
    print("Testing nthFibonacci()...", end="")
    assert(nthFibonacci(0) == 1)
    assert(nthFibonacci(1) == 1)
    assert(nthFibonacci(2) == 2)
    assert(nthFibonacci(3) == 3)
    assert(nthFibonacci(4) == 5)
    assert(nthFibonacci(5) == 8)
    assert(nthFibonacci(6) == 13)
    print("Passed.")

testNthFibonacci()

def distance(x1, y1, x2, y2):
    return ((x2-x1)**2 + (y2-y1)**2)**0.5

def circlesIntersect(x1, y1, r1, x2, y2, r2):
    d = distance(x1, y1, x2, y2)  #distance between two centers
    rtot = r1 + r2   #sum of radius
    if  (rtot>=d):
        return True
    else:
        return False

def testCirclesIntersect():
    print("Testing circlesIntersect()...", end="")
    assert(circlesIntersect(0, 0, 2, 3, 0, 2) == True)
    assert(circlesIntersect(0, 0, 2, 4, 0, 2) == True)
    assert(circlesIntersect(0, 0, 2, 5, 0, 2) == False)
    print("Passed.")

testCirclesIntersect()

import math

def leastPiError(n):
    m = round(n*math.pi)
    diff = abs(math.pi - m/n)
    return diff

def almostEqual(d1, d2):
    epsilon = 10**-8
    return (abs(d1 - d2) < epsilon)

def testLeastPiError():
    print("Testing leastPiError()...", end="")
    assert(almostEqual(leastPiError(  7), 0.0012644893)) # at 22/7
    assert(almostEqual(leastPiError( 43), 0.0020577699)) # at 135/43
    assert(almostEqual(leastPiError(113), 0.0000002668)) # at 355/113
    print("Passed.")
 
testLeastPiError()

def nearestOdd(n):
    y = round(n)
    if (n%2 ==1):
        return y
    else:
        a = abs((y+1)-n)
        b = abs(n-(y-1))
        if (b<=a):
            return y-1
        else:
            return y+1

def testNearestOdd():
    print("Testing nearestOdd()...", end="")
    assert(nearestOdd(13) == 13)
    assert(nearestOdd(12.001) == 13)
    assert(nearestOdd(12) == 11)
    assert(nearestOdd(11.999) == 11)
    assert(nearestOdd(-13) == -13)
    assert(nearestOdd(-12.001) == -13)
    assert(nearestOdd(-12) == -13)
    assert(nearestOdd(-11.999) == -11)
    print("Passed.")
 
testNearestOdd()

def eggCartons(eggs):
    return math.ceil(eggs/12)

def testEggCartons():
    print("Testing eggCartons()...", end="")
    assert(eggCartons(0) == 0)
    assert(eggCartons(1) == 1)
    assert(eggCartons(12) == 1)
    assert(eggCartons(13) == 2)
    assert(eggCartons(24) == 2)
    assert(eggCartons(25) == 3)
    print("Passed.")
 
testEggCartons()

def pittsburghHour2(londonHour):
    if (londonHour>=6 and londonHour<=17):
        return londonHour-5
    elif(londonHour>=18 and londonHour<=23):
        return londonHour-17
    else:
        return londonHour+7

def pittsburghHour(londonHour):
    PH = (londonHour-5)%12
    if PH == 0: return 12
    return PH

def testPittsburghHour():
    print("Testing pittsburghHour()...", end="")
                                     # London   Pittsburgh
    assert(pittsburghHour( 0) ==  7) # midnight    7pm
    assert(pittsburghHour( 5) == 12) #   5am      12am (midnight)
    assert(pittsburghHour(10) ==  5) #  10am       5am
    assert(pittsburghHour(12) ==  7) #  noon       7am
    assert(pittsburghHour(17) == 12) #   5pm       12pm (noon)
    assert(pittsburghHour(18) ==  1) #   6pm       1pm
    print("Passed.")

testPittsburghHour()

def areCollinear(x1, y1, x2, y2, x3, y3):
    # (x1 - x2 == 0 and x1 - x3 == 0):
       # return True
    if((y3 - y2)*(x3-x1) == (y3 - y1)*(x3-x2)):
        return True
    else:
        return False

def testAreCollinear():
    print("Testing testAreCollinear()...", end="")
    assert(areCollinear(0, 0, 1, 1, 2, 2) == True)
    assert(areCollinear(0, 0, 1, 1, 2, 3) == False)
    assert(areCollinear(1, 1, 0, 0, 2, 2) == True)
    assert(areCollinear(1, 1, 0, -1, 2, 2) == False)
    assert(areCollinear(2, 0, 2, 1, 2, 2) == True)
    assert(areCollinear(2, 0, 2, 1, 3, 2) == False)
    assert(areCollinear(3, 0, 2, 1, 3, 2) == False)
    print("Passed.")

testAreCollinear()

def numberOfPoolBalls(rows):
    return rows*(rows+1)/2 

def testNumberOfPoolBalls():
    print("Testing numberOfPoolBalls()...", end="")
    assert(numberOfPoolBalls(0) == 0)
    assert(numberOfPoolBalls(1) == 1)
    assert(numberOfPoolBalls(2) == 3)   # 1+2 == 3
    assert(numberOfPoolBalls(3) == 6)   # 1+2+3 == 6
    assert(numberOfPoolBalls(10) == 55) # 1+2+...+10 == 55
    print("Passed.")

testNumberOfPoolBalls()

def numberOfPoolBallRows(balls):
    return math.ceil((-1 + math.sqrt(1+8*balls))/2)

def testNumberOfPoolBallRows():
    print("Testing numberOfPoolBallRows()...", end="")
    assert(numberOfPoolBallRows(0) == 0)
    assert(numberOfPoolBallRows(1) == 1)
    assert(numberOfPoolBallRows(2) == 2)
    assert(numberOfPoolBallRows(3) == 2)
    assert(numberOfPoolBallRows(4) == 3)
    assert(numberOfPoolBallRows(6) == 3)
    assert(numberOfPoolBallRows(7) == 4)
    assert(numberOfPoolBallRows(10) == 4)
    assert(numberOfPoolBallRows(11) == 5)
    assert(numberOfPoolBallRows(55) == 10)
    assert(numberOfPoolBallRows(56) == 11)
    print("Passed.")

testNumberOfPoolBallRows()

def dayOfWeek(month, day, year):
    if (month ==1 or month ==2):
        month += 12
        year += -1
        N = day + 2*month + int(3*(month+1)/5) + year + int(year/4) - int(year/100) + int(year/400) +2
        if (N%7 == 0):
            return 7
        else:
            return N%7
    else:
        N = day + 2*month + int(3*(month+1)/5) + year + int(year/4) - int(year/100) + int(year/400) +2
        if (N%7 == 0):
            return 7
        else:
            return N%7

def testDayOfWeek():
    print("Testing dayOfWeek()...", end="")
    # On 2/5/2006, the Steelers won Super Bowl XL on a Sunday!
    assert(dayOfWeek(2, 5, 2006) == 1)
    # On 6/15/1215, the Magna Carta was signed on a Monday!
    assert(dayOfWeek(6, 15, 1215) == 2)
    # On 3/11/1952, the author Douglas Adams was born on a Tuesday!
    assert(dayOfWeek(3, 11, 1952) == 3)
    # on 4/12/1961, Yuri Gagarin became the first man in space, on a Wednesday!
    assert(dayOfWeek(4, 12, 1961) == 4)
    # On 7/4/1776, the Declaration of Independence was signed on a Thursday!
    assert(dayOfWeek(7, 4, 1776) == 5)
    # on 1/2/1920, Isaac Asimov was born on a Friday!
    assert(dayOfWeek(1, 2, 1920) == 6)
    # on 10/11/1975, Saturday Night Live debuted on a Saturday (of course)!
    assert(dayOfWeek(10, 11, 1975) == 7)
    print("Passed.")

testDayOfWeek()

import math

def sphereVolumeFromSurfaceArea(surfaceArea):
    r = math.sqrt(surfaceArea/(4*math.pi))
    volume = (4/3)*math.pi*r**3
    return volume

def almostEqual(d1, d2):
    epsilon = 10**-4
    return (abs(d1 - d2) < epsilon)

def testSphereVolumeFromSurfaceArea():
    print("Testing sphereVolumeFromSurfaceArea()...", end="")
    # From http://www.aqua-calc.com/calculate/volume-sphere, with r=3, we see:
    assert(almostEqual(sphereVolumeFromSurfaceArea(452.38934),  904.77868) == True) # r=6
    assert(almostEqual(sphereVolumeFromSurfaceArea(113.09734), 113.09734) == True) # r=3
    assert(almostEqual(sphereVolumeFromSurfaceArea(452.38934),  904) == False) # r=6
    assert(almostEqual(sphereVolumeFromSurfaceArea(452.38934),  905) == False) # r=6
    assert(almostEqual(sphereVolumeFromSurfaceArea(113.09734), 113) == False) # r=3
    assert(almostEqual(sphereVolumeFromSurfaceArea(113.09734), 113.1) == False) # r=3
    print("Passed.")

testSphereVolumeFromSurfaceArea()

import math

def almostEqual(d1, d2):
    epsilon = 10**-8
    return (abs(d1 - d2) < epsilon)

def isRightTriangle(x1, y1, x2, y2, x3, y3):
    s1 = distance(x1, y1, x2, y2)
    s2 = distance(x2, y2, x3, y3)
    s3 = distance(x1, y1, x3, y3)
    h3 = math.sqrt(s1**2 + s2**2)
    h2 = math.sqrt(s1**2 + s3**2)
    h1 = math.sqrt(s3**2 + s2**2)
    if (almostEqual(s1,h1) or almostEqual(s2,h2) or almostEqual(s3,h3)):
        return True
    else:
        return False


def testIsRightTriangle():
    print("Testing isRightTriangle()...", end="")
    assert(isRightTriangle(0, 0, 0, 3, 4, 0) == True)
    assert(isRightTriangle(1, 1.3, 1.4, 1, 1, 1) == True)
    assert(isRightTriangle(9, 9.12, 8.95, 9, 9, 9) == True)
    assert(isRightTriangle(0, 0, 0, math.pi, math.e, 0) == True)
    assert(isRightTriangle(0, 0, 1, 1, 2, 0) == True)
    assert(isRightTriangle(0, 0, 1, 2, 2, 0) == False)
    assert(isRightTriangle(1, 0, 0, 3, 4, 0) == False)
    print("Passed.")

testIsRightTriangle()
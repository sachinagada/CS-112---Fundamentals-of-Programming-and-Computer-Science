# hw2.py
# Sachi Nagada + snagada + 1,GG

import math

def almostEqual(d1, d2):
    epsilon = 10**-3
    return (abs(d2 - d1) < epsilon)

def isPrime(n):   # code from class. Url: http://www.cs.cmu.edu/~112/notes/notes-loops.html#isPrime
    if (n < 2):
        return False
    elif (n ==2):
        return True
    elif (n%2 ==0):
        return False
    maxfactor = round(math.sqrt(n))
    for term in range(2,maxfactor+1):
        if n%term==0:
            return False
    return True

def sumOfSquaresOfDigits(n):
    total = 0
    while (n> 0):
        onesdigit = n%10
        n//=10
        total += onesdigit**2
    return total

def isHappyNumber(n):
    if n<1:
        return False
    else:
        while n >= 1:
            n = sumOfSquaresOfDigits(n)
            if n==4:
                return False
            elif n ==1:
                return True
        return n

def nthHappyNumber(n):
    found = 0
    guess = 0
    while found<=n:
        guess +=1
        if isHappyNumber(guess):
            found +=1
    return guess

def nthHappyPrime(n):
    found = 0
    guess = 0
    while found <=n:
        guess +=1
        if isHappyNumber(guess) and isPrime(guess):
            found +=1
    return guess

def isKaprekaNumber(n):
    x = n**2
    count = 0
    while (x>=n):
        count +=1
        x //=10
        y = n**2 - x*(10**(count))
        if (y==0):
            continue
        total = x + y
        if (total ==n):
            return True
    return False

def nearestKaprekarNumber(n):
    for guess in range (n,0, -1):
        if isKaprekaNumber(guess):
            a = guess
            break
    for guess in range (n,n*n):
        if isKaprekaNumber(guess):
            b = guess
            break
    adiff = abs(a-n)
    bdiff = abs(b-n)
    if adiff>bdiff:
        return b
    else:
        return a

def nthCarolPrime(n):
    found = 0
    k = 1
    while (found<=n):
        y = ((2**k - 1)**2 - 2)
        if isPrime(y):
            found+=1
        k+=1
    return y


def carrylessAdd(x, y):
    total = 0
    count = 0
    big = max(x,y)
    small = min(x,y)
    while (big>0):
        a = big%10
        b = small%10
        add = (a+b)%10
        total += add*(10**count)
        count +=1
        big //=10
        small //=10
    return total

def carrylessMultiply(x, y):
    small = min(x,y)
    big = max(x,y)
    count1 = 0
    total2 = 0
    while (small>0):
        a = small%10
        big = max(x,y)
        count2 = 0
        total1 = 0
        while (big>0):
            b = big%10
            multiply = (a*b)%10
            total1 += multiply*(10**count2)*(10**count1)
            big//=10
            count2 += 1
        count1 += 1
        small //=10
        total2 = carrylessAdd(total2,total1)
    return total2

def integral(f, a, b, N):
    h = (b-a)/N
    count = 0
    totalarea = 0
    while (count<N):
        x = a + h
        area = (x-a)*(f(a)+f(x))/2
        totalarea +=area
        a = x
        count +=1
    return totalarea


######################################################################
# ignore_rest: The autograder will ignore all code below here
######################################################################

def testsumOfSquaresOfDigits():
    print("Testing sumOfSquaresOfDigits()...", end="")
    assert(sumOfSquaresOfDigits(5) == 25)   # 5**2 = 25
    assert(sumOfSquaresOfDigits(12) == 5)   # 1**2 + 2**2 = 1+4 = 5
    assert(sumOfSquaresOfDigits(234) == 29) # 2**2 + 3**2 + 4**2 = 4 + 9 + 16 = 29
    print("Passed.")

def testisHappyNumber():
    print("Testing isHappyNumber()...", end="")
    assert(isHappyNumber(-7) == False)
    assert(isHappyNumber(1) == True)
    assert(isHappyNumber(2) == False)
    assert(isHappyNumber(97) == True)
    assert(isHappyNumber(98) == False)
    assert(isHappyNumber(404) == True)
    assert(isHappyNumber(405) == False)
    print("Passed.")

def testnthHappyNumber():
    print("Testing nthHappyNumber()...", end="")
    assert(nthHappyNumber(0) == 1)
    assert(nthHappyNumber(1) == 7)
    assert(nthHappyNumber(2) == 10)
    assert(nthHappyNumber(3) == 13)
    assert(nthHappyNumber(4) == 19)
    assert(nthHappyNumber(5) == 23)
    assert(nthHappyNumber(6) == 28)
    assert(nthHappyNumber(7) == 31)
    print("Passed.")

def testnthHappyPrime():
    print("Testing nthHappyPrime() ...", end="")
    assert(nthHappyPrime(0)==7)
    assert(nthHappyPrime(1)==13)
    print("Passed.")

def testnearestKaprekarNumber():
    print("Testing nearestKaprekarNumber()...", end="")
    assert(nearestKaprekarNumber(49) == 45)
    assert(nearestKaprekarNumber(51) == 55)
    assert(nearestKaprekarNumber(50) == 45)
   # assert(nearestKaprekarNumber(1)==1)
    print("Passed.")

def testnthCarolPrime():
    print("Testing nthCarolPrime()...", end="")
    assert(nthCarolPrime(0) == 7)
    assert(nthCarolPrime(1) == 47)
    assert(nthCarolPrime(2) == 223)
    assert(nthCarolPrime(3) == 3967)
    assert(nthCarolPrime(4) == 16127)
    assert(nthCarolPrime(5) == 1046527)
    assert(nthCarolPrime(6) == 16769023)
    print("Passed.")

def testcarrylessAdd():
    print("Testing carrylessAdd()...", end="")
    assert(carrylessAdd(785, 376==51))
    assert(carrylessAdd(4,9 ==3))
    print("Passed.")

def testcarrylessMultiply():
    print("Testing carrylessMultiply()...", end="")
    assert(carrylessMultiply(643, 59)==417)
    print("Passed.")

def g(x):
    return x

def h(x):
    return 2*x**2

def testintegral():
    print("Testing integral()...", end="")
    assert(almostEqual(integral(g,2,4,10),6))
    assert(almostEqual(integral(h,0,3,210),18))
    print("Passed.")

def testAll():
    testsumOfSquaresOfDigits()
    testisHappyNumber()
    testnthHappyNumber()
    testnthHappyPrime()
    testnearestKaprekarNumber()
    testnthCarolPrime()
    testcarrylessAdd()
    testcarrylessMultiply()
    testintegral()

testAll()

# if __name__ == "__main__":
   # testAll()


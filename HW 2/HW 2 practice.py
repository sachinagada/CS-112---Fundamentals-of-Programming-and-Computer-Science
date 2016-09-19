import math

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

def nthPrime(n):  # from class notes, same URL as is prime
    found = 0
    guess = 0
    while (found <= n):
        guess += 1
        if (isPrime(guess)):
            found += 1
    return guess

def digitCount(n):
    n = abs(n)
    counter = 1
    while (n>=10):
        counter += 1
        n //= 10
    return counter

def getdigitcount(n,digit):
    digitcount2 = 0
    while n > 0:
        onesdigit = n%10
        n//=10
        if (onesdigit == digit):
            digitcount2 +=1
    return digitcount2

def mostFrequentDigit(n):
    n = abs(n)
    bestcount = 0
    for digit in range(10):
        digitcount = getdigitcount(n,digit)
        if (digitcount > bestcount):
            bestdigit = digit
            bestcount = digitcount
    return bestdigit

def isRotation(x, y):
    if x == y:
        return True
    digits = digitCount(y)
    for i in range(1,digits):
        yfront = y//(10**(digits-i))
        yback = y - (yfront*(10**(digits-i)))
        yrotated = (yback*(10**i)) + yfront
        if yrotated ==x:
            return True
    return False

def testisRotation():
    print("Testing sRotation()...", end="")
    assert(isRotation(1234,3412)==True)
    assert(isRotation(321,3210)==True)
    assert(isRotation(123,321)==False)
    print("Passed.")

def hasOnlyOddDigits(n):
    n = abs(n)
    while n>0:
        x = n%10
        if (x%2 ==0):
            return False
        n //=10
    return True

def hasConsecutiveDigits(n): 
    n = abs(n)
    if (n<10):
        return False
    while (n>=10):
        x = n%10
        y = (n//10)%10
        if (x==y):
            return True
        n //= 10
    return False

def longestDigitRun(n): 
    n = abs(n)
    longestcount = 0
    longestdigit = 0
    digits = digitCount(n)
    count = 0
    for i in range(digits):
        ncurrent = (n//(10**i))%10
        nnext = (n//(10**(i+1)))%10
        if ncurrent == nnext:
            count +=1
        elif ncurrent != nnext:
            count = 0
        if count > longestcount:
            longestcount = count
            longestdigit = ncurrent
        if (count ==longestcount) and (ncurrent < longestdigit):
            longestdigit = ncurrent
    return longestdigit

def testlongestDigitRun():
    print("Testing longestDigitRun()...", end="")
    assert(longestDigitRun(117773732)==7)
    assert(longestDigitRun(-677886)==7)
    print("Passed.")


def isPalindrome(n):
    digits = digitCount(n)
    for term in range(1,digits+1,2):
        x = n%10
        y = (n//(10**(digits-term)))%10
        if (x==y):
            n = (n - x - y*(10**(digits-term)))//10
        else:
            return False
    return True

def nthPalindromicPrime(n):
    found = -1
    guess = 0
    while (found<n):
        guess +=1
        if isPalindrome(guess) and isPrime(guess):
            found +=1
    return guess

def isLeftTruncatablePrime(n):
    while (n>0):
        if isPrime(n):
            digit = digitCount(n)
            firstdigit = (n//10**(digit-1))
            n = n - firstdigit*(10**(digit-1))
        else:
            return False
    return True

def nthLeftTruncatablePrime(n):
    found = 0
    guess = 1
    while (found<=n):
        guess +=1
        if isLeftTruncatablePrime(guess):
            found +=1
    return guess

print(nthLeftTruncatablePrime(16))

def pi(n):  #counting Prime numbers
    found = 0
    for term in range (2, n+1):
        if (isPrime(term)):
            found +=1
    return found

def h(n):  #harmonic number
    if n<=0:
        return 0
    total = 0
    for term in range(1,n+1):
        total += 1/term
    return total

def testh():
    print("Testing h()...", end="")
    assert(almostEquals(h(0),0.0))
    assert(almostEquals(h(1),1/1.0))  # h(1) = 1/1
    assert(almostEquals(h(2),1/1.0 + 1/2.0))  # h(2) = 1/1 + 1/2
    assert(almostEquals(h(3),1/1.0 + 1/2.0 + 1/3.0))  # h(3) = 1/1 + 1/2 + 1/3
    print ("Passed all tests!")

def estimatedPi(n):
    if n<=2:
        return 0
    elif type(n)==int:
        return int(round(n/(h(n)-1.5)))
    return 42

def estimatedPiError(n):
    if n<=2:
        return 0
    estimpi = estimatedPi(n)
    actual = pi(n)
    return abs(estimpi - actual)

def sign(n):
    if n<0:
        return -1
    elif n>0:
        return +1

def f(x):
    return x**5 - 2**x

def findZerosWithBisection(x0,x1,epsilon):
    if (f(x0) ==0):
        return x0
    elif f(x1) == 0:
        return x1
    elif sign(f(x0)) == sign(f(x1)):
        return None
    while (abs(x1-x0)>=epsilon):
        xmid = (x0 + x1)/2
        if f(xmid)==0:
            return xmid
        elif (sign(f(xmid))==sign(f(x0))):
            x0 = xmid
        else:
            x1 = xmid
    return (x0+x1)/2

def isPowerfulNumber(n):
    numberofprimes = pi(n)
    for i in range(numberofprimes):
        primenumber = nthPrime(i)
        if (n%primenumber==0):
            if (n%(primenumber**2)!=0):
                return False
            else:
                continue
    return True

def nthPowerfulNumber(n):
    found = 0
    guess = 0
    while (found<=n):
        guess += 1
        if isPowerfulNumber(guess):
            found +=1
    return guess
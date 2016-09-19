# hw8b.py
# Sachi Nagada + snagada + 1,GG

import math

#isPrime from class notes on recursion part 1
#http://www.cs.cmu.edu/~112/notes/notes-recursion-part1.html

def isPrime(n, factor=2):
    if (n < 2): return False
    elif (factor*factor > n): return True
    elif (n % factor == 0): return False
    else: return isPrime(n, factor+1)

def hasZero(n): #won't work for 0 but guesses start at 1
    if n<10: #everything less than 10 and greater than 0 doesn't have a 0
        return False
    else:
        right = n%10 # the right most digit
        left = n//10 # rest of the number
        if right ==0:
            return True
        else:
            return hasZero(left) #checks the rest of the number for 0s

def isLeftTruncatablePrime(n):
    numberofDigits = math.ceil(math.log(n)/math.log(10))
    if numberofDigits ==1:
        return isPrime(n)
    #it either has a 0 or is not a prime
    if isPrime(n)==False or hasZero(n)==True: return False
    else:
        leftDigit = n//(10**(numberofDigits-1))
        #rest of the number without the leftmost digit
        truncatedPrime = n- (leftDigit * (10**(numberofDigits-1)))
        #checks the rest of the number for being left Truncated Prime
        return isLeftTruncatablePrime(truncatedPrime)

def nthLeftTruncatablePrime(n,found = 0, guess = 1):
    #found has to be n+1 to make up for n=0 and guess - 1 because added 1 
    # to guess for the next recursion call
    if (found == n+1): return guess-1 
    if (isLeftTruncatablePrime(guess)): #found a truncated prime
        return nthLeftTruncatablePrime(n, found+1, guess+1)
    else: # keep on going through all the numbers until n found
        return nthLeftTruncatablePrime(n, found, guess+1)

def carrylessAdd(x, y,count=0, result = 0):
    if x==0 and y==0: #keeps on adding until both digits are 0
        return result
    else:
        right1 = x%10 #the right most digit of the two numbers
        right2 = y%10 
        summation = (right1 + right2)%10 # no carryons are kept affter adding
        result += summation*(10**count) #count kept to keep digits place
        left1 = x//10 
        left2 = y//10
        #carrylessly adds the remaining parts of the numbers
        return carrylessAdd(left1, left2, count+1, result)


def getMin(n,low = ""):
    n = abs(n)
    if n ==0: # if n is 0 to begin with, low would be empty string
        if low=="":
            low = 0
        return low
    else:
        right = n%10
        if low=="" or right<low: #gives low a value the first run 
            low = right
        return getMin(n//10,low)


def longestDigitRun(n, last=None, count=0, bestRun = -1, longestDigit = None):
    n = abs(n)
    if n==0:
        if longestDigit==None: #if n is 0 to begin with, longestDig = None
            longestDigit = 0 # so it needs to change
        return longestDigit
    else:
        right = n%10 #the right most digit
        if right == last: #compares to the last digit
            count +=1
            if count > bestRun: #replaces bestRun when count gets bigger
                bestRun = count
                longestDigit = right #replaces longest digit 
            elif count == bestRun:
                # the longestDigit will be a digit and not none at this point
                # because it changes after the first consecutive case
                longestDigit = min(longestDigit, last)
            return longestDigitRun(n//10, last, count, bestRun, longestDigit)
        else:
            if bestRun == -1: #this way the longestDigit has a value and
                bestRun +=1   # best run will be 0 unless consecutive
                longestDigit = getMin(n)
            #the count has to go back to zero to not confuse with run of
            #another digit
            count = 0 
            last = right #the last digit to compare has to change as well
            return longestDigitRun(n//10, last, count, bestRun, longestDigit)

#from class notes on string
# http://www.cs.cmu.edu/~112/notes/notes-strings.html
def isPalindrome(s):
    return s == s[::-1]

def longestSubstring(s1, s2):
    len1 = len(s1)
    len2 = len(s2)
    if len1>len2: #s1 is longer
        return s1
    elif len1 == len2:
        return max(s1, s2)
    else: #s2 is longer
        return s2


def longestSubpalindrome(s, subString = "None", longestSub="", startIndex=0, 
                                                                endIndex=0):
    #base case when the string is done chopping
    if subString =="": 
        longestSub = longestSubstring(subString,longestSub)
        return longestSub
    elif isPalindrome(subString):
        #compares to the longestSub to see if its bigger/longer
        longestSub = longestSubstring(subString,longestSub)
        #checks the rest of the string and iterates through the endIndex until
        #the endIndex is the length of hte string and then it changes the 
        #startIndex
        if endIndex == len(s)+1:
            startIndex +=1
            endIndex = startIndex+1
        #if endIndex isn't the length, then just add one to the string
        else:
            endIndex += 1
        subString = s[startIndex: endIndex]
        return longestSubpalindrome(s, subString, longestSub, startIndex, 
            endIndex)
    #not a palindrome and checks the rest of the string/substrings
    else:
        #same string chopping method as above to check all the combos
        if endIndex == len(s)+1:
            startIndex +=1
            endIndex = startIndex+1
        else:
            endIndex += 1
        subString = s[startIndex: endIndex]
        return longestSubpalindrome(s, subString, longestSub, startIndex, 
            endIndex)

######################################################################
# ignore_rest: The autograder will ignore all code below here
######################################################################

def testisLeftTruncatablePrime():
    print("Testing isLeftTruncatablePrime...",end = "")
    assert(isLeftTruncatablePrime(2)==True)
    assert(isLeftTruncatablePrime(617)==True)
    assert(isLeftTruncatablePrime(618)==False)
    print("Passed.")


def testhasZero():
    print("Testing hasZero...", end="")
    assert(hasZero(9)==False)
    assert(hasZero(10)==True)
    assert(hasZero(987)==False)
    assert(hasZero(34098)==True)
    print("Passed.")

def testnthLeftTruncatablePrime():
    print("Testing nthLeftTruncatablePrime...",end="")
    assert(nthLeftTruncatablePrime(0)==2)
    assert(nthLeftTruncatablePrime(10)==53)
    assert(nthLeftTruncatablePrime(15)==113)
    print("Passed.")

def testcarrylessAdd():
    print("Testing carrylessAdd()...", end="")
    assert(carrylessAdd(785, 376==51))
    assert(carrylessAdd(4,9 ==3))
    assert(carrylessAdd(5,5)==0)
    assert(carrylessAdd(785,76)==751)
    print("Passed.")

def testgetMin():
    print("Testing getMin...",end="")
    assert(getMin(123)==1)
    assert(getMin(321)==1)
    assert(getMin(-1023)==0)
    assert(getMin(0)==0)
    print("Passed.")

def testlongestDigitRun():
    print("Testing longestDigitRun...",end="")
    assert(longestDigitRun(117773732)==7)
    assert(longestDigitRun(1122)==1)
    assert(longestDigitRun(321)==1)
    assert(longestDigitRun(1111)==1)
    assert(longestDigitRun(103)==0)
    assert(longestDigitRun(0)==0)
    print("Passed.")

def testlongestSubstring():
    print("Testing longestSubstring...",end="")
    assert(longestSubstring("acde","bcaad")=="bcaad")
    assert(longestSubstring("acd", "dca")=="dca")
    assert(longestSubstring("","")=="")
    print("Passed.")

def testlongestSubpalinddrome():
    print("Testing longestSubpalindrome...",end="")
    assert(longestSubpalindrome("ab-4-be!!!")=="b-4-b")
    assert(longestSubpalindrome("abcbce")== "cbc")
    assert(longestSubpalindrome("")== "")
    assert(longestSubpalindrome("a")== "a")
    print("Passed.")

def testAll():
    testhasZero()
    testisLeftTruncatablePrime()
    testnthLeftTruncatablePrime()
    testcarrylessAdd()
    testlongestDigitRun()
    testlongestSubstring
    testgetMin()
    testlongestSubpalinddrome()
testAll()
# if __name__ == "__main__":
   # testAll()

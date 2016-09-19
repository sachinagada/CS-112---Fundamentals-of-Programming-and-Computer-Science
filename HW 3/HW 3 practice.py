import string

def sameChars(s1, s2):
    for c in s1:
        if c not in s2:
            return False
    for c in s2:
        if c not in s1:
            return False
    return True

def testsameChars():
    print("Testing sameChars()...", end="")
    assert(sameChars("cat", "CAT") == False)
    assert(sameChars("cat", "tca") == True)
    assert(sameChars("tca", "caT") == False)
    assert(sameChars("tcaactacttca", "cat") == True)
    print("Passed.")

testsameChars()

def wordWrap(text, width):
    result = ""
    numberoflines = len(text)//width
    for i in range(numberoflines):
        result += text[width*i:width*(i+1)]+"\n"
    result += text[width*numberoflines:]
    count1 = result.count(" \n")
    count2 = result.count("\n ")
    while count1 > 0 and count2 > 0:
        result = result.replace(" \n", "\n")
        result = result.replace("\n ","\n")
        count1 = result.count(" \n")
        count2 = result.count("\n ")
        
    result = result.replace(" ", "-")
    return result

def testwordWrap():
    print("Testing sameChars()...", end="")
    assert(wordWrap("abcdefghij", 4)  ==  """\
abcd
efgh
ij""")
    assert(wordWrap("a b c de fg",  4)  ==  """\
a-b
c-de
fg""")
    print("Passed.")

testwordWrap()

def largestNumber(text):
    largest = "0"
    result = ""
    for c in text:
        if c.isdigit():
            result += c
        else:
            result += ","
    for number in result.split(","):
        if len(number) > len(largest) :
            largest = number
        elif len(number)==len(largest) and number > largest:
            largest = number
    if largest == "0":
        return None
    return int(largest)

def testlargestNumber():
    print("Testing largestNumber()...", end="")
    assert(largestNumber("I saw 3 dogs, 17 cats, and 14 cows!") == 17)
    assert(largestNumber("One person ate two hot dogs!") == None)
    print("Passed.")

testlargestNumber()

def isPalindrome(s):
    return (s == s[::-1])

def longestSubpalindrome(s):
    longestsub = ""
    for startindex in range (len(s)):
        for endindex in range((startindex+1),(len(s)+1)):
            substring = s[startindex:endindex]
            if isPalindrome(substring):
                if (len(substring) > len(longestsub)):
                    longestsub = substring
                elif (len(substring)==len(longestsub)):
                    if (substring>s):
                        longestsub = substring
    return longestsub

def testlongestSubpalndrome():
    print("Testing longestSubpalindrome()...", end="")
    assert(longestSubpalindrome("ab-4-be!!!") == "b-4-b")
    assert(longestSubpalindrome("abcbce") ==  "cbc")
    print("Passed.")

testlongestSubpalndrome()

def longestCommonSubstring(s1, s2):
    longest = ""
    for startindex in range(len(s1)):
        for endindex in range((startindex+1), (len(s1)+1)):
            substring = s1[startindex:endindex]
            if substring in s2:
                if len(substring) > len(longest):
                    longest = substring
                elif len(substring) == len(longest):
                    if substring < longest:
                        longest = substring
    return longest

def testlongestCommonSubstring():
    print("Testing longestCommonSubstring()...", end="")
    assert(longestCommonSubstring("abcdef", "abqrcdest") == "cde")
    assert(longestCommonSubstring("abcdef", "ghi") == "")
    assert(longestCommonSubstring("abcABC", "zzabZZAB") == "AB")
    print("Passed.")

testlongestCommonSubstring()

def leastFrequentLetters(s):
    least = 5
    leastletter = ""
    s = s.lower()
    for c in string.ascii_lowercase:
        if c in s:
            count = s.count(c)
            if count < least:
                least = count
                leastletter = c
            elif count == least:
                leastletter += c
    return leastletter

def testleastFrequentLetters():
    print("Testing leastFrequentLetters()...", end="")
    assert(leastFrequentLetters("aDq efQ? FB'daf!!!")  == "be")
    print("Passed.")

testleastFrequentLetters()

def replace(s1, s2, s3):
    place = s1.find(s2)
    result = s1[:place]+ s3 + s1[(place+len(s2)):]
    return result

def testreplace():
    print("Testing replace()...", end="")
    assert(replace("Hi Sachi","Hi","sup")  == "Hi Sachi".replace("Hi", "sup"))
    print("Passed.")

testreplace()

def encrpyt(plaintext, password):
    if password.islower()==False:
        return "password must be all lowercase"
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    s1 = plaintext.upper()
    result=""
    for c in s1:
        if c in string.ascii_uppercase:
            result += c
    s1new = result
    answer = ""
    for i in range(len(s1new)):
        index = uppercase.find(s1new[i])
        shift = lowercase.find(password[(i%len(password))])
        answer += uppercase[((index+shift)%26)]
    return answer

print(encrpyt("Go team!","azby"))

def decrypt(plaintext, password):
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    answer = ""
    for i in range(len(plaintext)):
        index = uppercase.find(plaintext[i])
        shift = lowercase.find(password[(i%len(password))])
        answer += uppercase[((index-shift)%26)]
    return answer

print(decrypt("GNUCAL", "azby"))

def isValidHand(s):
    if len(s) != 14:
        return False
    ranks = "TJQKA23456789"
    suit = "HDCS"
    for entry in s.split(" "):
        if entry[0] not in ranks:
            return False
        if entry[1] not in suit:
            return False
    return True


def isFlush(s):
    if isValidHand(s) == False:
        return False
    suit = ""
    possibilities = "H"*5 + "D"*5 + "C"*5 + "S"*5
    for entry in s.split(" "):
        suit += entry[1]
    if suit not in possibilities:
        return False
    return True

def isRoyalFlush(s):
    if isValidHand(s) == False:
        return False
    if isFlush(s) == False:
        return False
    rank = "TJQKA"
    for entry in s.split(" "):
        index = rank.find(entry[0])
        if (index == -1):
            return False
        rank = rank.replace(entry[0],"")
    return True

def hasPair(s):
    if isValidHand(s) == False:
        return False
    rank = ""
    for entry in s.split(" "):
        rank += entry[0]
    for c in rank:
        count = rank.count(c)
        if count >= 2:
            return True
    return False

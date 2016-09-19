import copy

def median(a):
    if a == []:
        return None
    b = sorted(a)
    if (len(b)%2 == 1):
        return b[(len(b)//2)]
    else:
        average = (b[(len(b)//2)] + b[((len(b)//2)+1)])/2
        return average

def alternatingSum(a):
    odd = []
    even = []
    for i in range(len(a)):
        if i%2==0:
            even.append(a[i])
        else:
            odd.append(a[i])
    oddsum = sum(odd)
    evensum = sum(even)
    return evensum - oddsum

def mostCommonName(a):
    b = sorted(a)
    Commonname = []
    mostCount = None
    for name in b:
        count = b.count(name)
        if mostCount == None or count > mostCount:
            if name not in Commonname:
                mostCount = count
                Commonname = name
            elif count == mostCount:
                Commonname += name
    return Commonname

#print(mostCommonName(["Jane", "Aaron", "JANE", "Aaron"]))

def isRotation(a1, a2):
    if a1 == a2:
        return True
    for i in range(1,len(a1)):
        front = a1[:i]
        back = a1[i:]
        rotated = back + front
        if rotated == a2:
            return True
    return False

#print(isRotation([2,3,4,5],[4,5,2,3]))

def missingNumber(a):
    maximum = max(a)
    b = list(range(1,maximum+1))
    for num in a:
        b.remove(num)
    return b

#print(missingNumber([1,4,3,5,8,9,7,6]))

def split(a1,a2):
    a1 = a1+a2
    delimiters = a1.count(a2)
    result = list(range(delimiters))
    count = 0
    string = ""
    for c in a1:
        if c != a2:
            string += c
        else:
            result[count]=string
            count +=1
            string =""
    return result
#print(split("ab,cd,efg", ","))

def join(a1,a2):
    result = ""
    for term in a1:
        result += term + a2
    n = len(result)
    result = result[:n-1]
    return result

#print(join(["ab", "cd", "efg"], ","))


def nondestructiveRotateList(a, n):
    n = -n
    b = a[n:] + a[:n]
    return b

def testNonDestructiveRotateList():
    print("Testing...nondestructiveRotateList()")
    assert(nondestructiveRotateList([1,2,3,4], 1) == [4,1,2,3])
    assert(nondestructiveRotateList([4,3,2,6,5], 2) == [6, 5, 4, 3, 2])
    assert(nondestructiveRotateList([1,2,3], 0) == [1,2,3])
    assert(nondestructiveRotateList([1, 2, 3], -1) == [2, 3, 1])
    print("Passed.")

#testNonDestructiveRotateList()

def destructiveRotateList(a, n):
    n = -n
    length = len(a)
    a.extend(a[:n])
    startindex = (length + n)%length
    a[:startindex] = []


#a = [1, 2, 3,4]
#print(destructiveRotateList(a, 1))
#print(a)

def histogram(a):
    return 42

'''assert(histogram([73, 62, 91, 74, 100, 77]) == """\
60-69: *
70-79: ***
80-89:
90++ : **
""")'''

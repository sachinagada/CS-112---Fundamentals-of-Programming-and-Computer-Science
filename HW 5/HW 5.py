# hw5.py
# Sachi Nagada + snagada + 1,GG

"""
slow1(a): 
1. this function counts the number of elements in list a
2. Worst-case big oh will be O(n) because one number is counted through each 
pass in the while loop and n passes will have to occur in order to count the 
elements. The steps inside the while loop have O(1) because pop is constant and
adding an integer to c is also constant. So overall the big oh will be n. Can 
be proven by timing it and seeing the linear increase in time with linear
increase in the list size.
3. len(a)
4. The big oh for len(a) is O(1) because when a list is made if python, it 
remembers the length of the list like a characteristic associated with the list
so when you call for len(a), it references what is already found. Can be proven
by barely seeing the change in time with increase in list length

slow2(a):
1. it returns true if there are no repeating elements in the list and false if 
there are repeating elements in the list.
2. Worst-case O(n**2) because the outer loop (for i) runs through n times 
and the inner loop (the one for j) runs through n for each run in the outer
loop. So it runs n * n times == O(n**2). Can prove by seeing the time
increase around 4 times for doubling the list length.
3.
def faster2(a):
    seen = set()
    for elem in a:
        if elem in seen:
            return False
        else:
            seen.add(elem)
    return True
4. O(n) because it only runs through the list once and checking for membership
in sets is constant. Can prove by linearly increasing the size of list and
 seeing the time increase linearly as well (0.01s for 50000 to 0.1s for 500000)

 slow3:
 1. Returns how many elements are in list b but not list a
 2. O(n**2) because the for loop runs n times and the checking for membership
 in the if loop requires going through the whole list. So n runs in the if loop
 for n times in the for loop gives O(n**2). Can prove by seeing the time 
 increase by four times for doubling the list size. 
 3. 
 def faster3(a,b):
    n = len(a)
    assert(n == len(b))
    seta = set(a)
    setb = set(b)
    diff = setb - seta
    return diff
 4. O(n) because creating seta will be n since it has to go through the list a
 and same with creating setb. Diff has a O(len(b) which is O(n) so the three 
together gives O(3n) == O(n). Can prove by increasing list length from 5000 to 
10000 and time going from 0.123 to 0.265. 

slow4:
1. Finds the biggest difference between any two elements in different lists. 
2. O(n**2) because the for loop for a runs n times and the for loop for b runs
n times. Since they are nested, they are multiplied so n*n = n**2. Prove by
timing. List of length 8000 takes 3.13 seconds and 16000 takes 12.81 seconds so
four times increase in time for doubling the list length
3.
def slow4(a, b):
    # assume a and b are the same length n
    n = len(a)
    assert(n == len(b))
    sorta = sorted(a)
    sortb = sorted(b)
    result = max(abs(sortb[n-1] - sorta[0]),abs(sorta[n-1]-sortb[0]))
4. O(nlogn) because it sorts the two lists giving 2nlogn and the max only has
to go through two values. Prove by timing. Takes 0.125s for 800,000 list length
and 1.26 for 8,000,000 so increases slightly greater increase due to the logn.

slow5:
1.Determines the smallest difference possible between any two elements of the
two list.  
2. O(n**2) because the for loop for a runs n times and the for loop for b runs
n times. Since they are nested, they are multiplied so n*n = n**2. Prove by
timing. List of length 8000 takes 12.37s and 4000 takes 3.106 seconds so time
decreases by four times by halving the list length.
3.
import bisect

def faster5(a,b):
    c = sorted(a)
    n = len(c)
    assert(n==len(b))
    result = None
    for elem in b:
        if (elem<c[n-1] and elem > c[0]):
            i = bisect.bisect(c,elem)
            diff = min((abs(c[i] - elem), abs(c[i-1]-elem)))
        elif elem >= c[n-1]:
            diff = elem - c[n-1]
        elif (elem <= c[0]):
            diff = c[0] - elem
        if result == None or diff<result:
            result = diff
    return result
4.O(nlogn) because the sort is nlogn and the going through the list b is n.
Adding the two together gives n+nlogn and O(n+nlogn) = O(nlogn). Prove by
timing. For list of length 4000, it took 0.0029s. For length of list 16000,
it took 0.100 which is a little more than linear increase due to logn
"""

def invertDictionary(d):
    newdict = dict()
    for key in d:
        newkey = d[key]  #the key of new dictionary will be value of d
        newvalue = set([key]) #the value of newdict will be the key of d
        if newkey not in newdict: #assigns value and key if key not in dict
            newdict[newkey] = newvalue
        elif newkey in newdict: #add the value to the set if key already exists
            (newdict[newkey]).add(key)
    return newdict

def friendsOfFriends(d):
    newdict = dict()
    d1 = d.copy() #creates a copy to be non destructive
    for key1 in d1:
        friends = d1[key1] #value will be list of friends
        if friends == set():
            newdict[key1] = set()
            continue
        for key2 in d1:
            if key2 in friends:
                newfriends = d1[key2] #friends of another person
            # subtracts set(key1) because their own name would appear otherwise
                fof = newfriends - friends - set([key1]) 
            # the value will be the union of the fof and the previous value. If
            # no previous value, the value will be empty set and more values 
            # will be added after the union
                newdict[key1]= newdict.get(key1,set()).union(fof)
    return newdict

def largestSumOfPairs(a):
    n = len(a)
    if n <= 1:  # if list is size 1 or smaller, returns None
        return None
    else:
        b = sorted(a) # sorts the list so largest numbers are in the end
        largestsum = b[n-1] + b[n-2] # adds the two largest numbers of the list
    return largestsum

def containsPythagoreanTriple(a):
    s = set()
    n = len(a)
    for elem in a:
        s.add(elem**2) #makes a list with squared values of the list elements
    for i in range(n-1): # goes to n-1 because problem for j when at n
        for j in range(i+1,n): #the values before i have been tested already
            if (a[i]**2 + a[j]**2) in s:
                return True #checks to see if the square value in the set
    if s == set():
        return False #if empty set, then no pythagorean triple
    return False

""" It takes 0.536s for the mergeSortWithOneAuxList with list with 50,000 
elements and 0.538s for the mergeSort with list with 50,000. increasing
the number of elements does not have a significant impact on the times so the 
change is not worthwhile."""

def merge(a, start1, start2, end, aux): # from class with few changes
    index1 = start1
    index2 = start2
    for i in range(len(aux)): # changed length to len(aux)
        if ((index1 == start2) or
            ((index2 != end) and (a[index1] > a[index2]))):
            aux[i] = a[index2]
            index2 += 1
        else:
            aux[i] = a[index1]
            index1 += 1
    for i in range(start1, end):
        a[i] = aux[i - start1]

def mergeSortWithOneAuxList(a):
    n = len(a)
    step = 1
    while (step < n):
        for start1 in range(0, n, 2*step):
            start2 = min(start1 + step, n)
            end = min(start1 + 2*step, n)
            length = end - start1
            aux = [None] * length #created the aux list here
            merge(a, start1, start2, end, aux) # pass the aux as a parameter
        step *= 2

def merge2(a, start1, start2, start3, end):
    index1 = start1
    index2 = start2
    index3 = start3
    length = end - start1
    aux = [None] * length
    for i in range(length): 
        if (index1 == start2): #if no numbers in the first block
            if index2!= start3:
                if index3 != end and a[index3]<a[index2]:
                    aux[i] = a[index3]
                    index3+=1
                else: #either a[index3] > a[index2] or index3 == end
                    aux[i] = a[index2]
                    index2+=1
            else: # index2==start3 only numbers in block 3 left
                aux[i] = a[index3]
        elif (index2 == start3):
            if index1 != start2:
                if (index3 != end) and (a[index3] < a[index1]):
                    aux[i] = a[index3]
                    index3+=1
                else: #either a[index3] > a[index1] or index3 == end
                    aux[i] = a[index1]
                    index1+=1
            else: # index 1 == start2 so only numbers in block 3 left
                aux[i] = a[index3]
                index3+=1
        elif (index3==end): 
            if index1 != start2 and a[index2] < a[index1]:
                aux[i] = a[index2]
                index2 += 1
            else: # index1 == start2 so only numbers in block 1 left
                aux[i] = a[index1]
                index1 +=1
        else: #find the minimum when the above conditions aren't met
            if (a[index1] <= a[index2] and a[index1] <= a[index3]):
                aux[i] = a[index1]
                index1+=1
            elif (a[index2] <= a[index1] and a[index2] <= a[index3]):
                aux[i] = a[index2]
                index2+=1
            elif (a[index3] <= a[index1] and a[index3] <= a[index1]):
                aux[i] = a[index3]
                index3+=1
    for i in range(start1, end):
        a[i] = aux[i - start1]

def threeWayMergesort(L):
    n = len(L)
    step = 1
    while (step < n):
        for start1 in range(0, n, 3*step): #runs by 3 step
            start2 = min(start1 + step, n) #determines the start for subsets
            start3 = min(start1 + 2*step, n)
            end = min(start1 + 3*step, n)
            merge2(L, start1, start2, start3, end)
        step *= 3

a = [12,35,22,2,92,6,42,58,9,8,1,3,4,7,100]
threeWayMergesort(a)
print(a)


######################################################################
# ignore_rest: The autograder will ignore all code below here
######################################################################

def testinvertDictionary():
    print("Testing invertDictionary()...",end="")
    assert(invertDictionary({1:2, 2:3, 3:4, 5:3}) == 
       {2:set([1]), 3:set([2,5]), 4:set([3])})
    assert(invertDictionary({1:2, 2:3, 3:4, 4:5}) ==
        {2:set([1]), 3:set([2]), 4:set([3]), 5:set([4])})
    assert(invertDictionary({})=={})
    print("Passed.")

def testfriendsOfFriends():
    print("Testing friendsOfFriends()...",end="")
    assert(friendsOfFriends({"fred":set(["wilma", "betty", "barney", 
        "bam-bam"]),"wilma":set(["fred", "betty", "dino"])})== 
    {'fred': {'dino'}, 'wilma': {'bam-bam', 'barney'}})
    assert(friendsOfFriends({"a":{"b","c","d"},
        "b":{"a","c","d","e"}, "c":{"a","b","f"}})== {'c': {'d', 'e'}, 
    'b': {'f'}, 'a': {'e', 'f'}})
    assert(friendsOfFriends({'A': {'B', 'D', 'F'}, 'B': {'A', 'C', 'D', 'E'},
     'C': set(), 'D': {'B', 'E', 'F'}, 'E': {'C', 'D'}, 'F': {'D'}}) == 
    {'F': {'E', 'B'}, 'E': {'F', 'B'}, 'C': set(), 'D': {'A', 'C'}, 
    'A': {'E', 'C'}, 'B': {'F'}})
    print("Passed.")

def testlargestSumOfPairs():
    print("Testing largestSumOfPairs()...",end="")
    assert(largestSumOfPairs([8,4,2,8])==16)
    assert(largestSumOfPairs([2])== None)
    assert(largestSumOfPairs([1,1,1,1])==2)
    print("Passed.")

def testcontainsPythagoreanTriple():
    print("Testing containsPythagoreanTriple()...",end="")
    assert(containsPythagoreanTriple([1,3,6,2,5,1,4])==True)
    assert(containsPythagoreanTriple([])== False)
    assert(containsPythagoreanTriple([1,2,3])==False)
    print("Passed.")

def testmergeSortWithONeAuxList():
    print("Testing mergeSortWithOneAuxList...",end ="")
    # test to see if it sorts a list with repeating numbers
    a = [2,6,3,4,9,10,2,1,4]
    mergeSortWithOneAuxList(a)
    assert(a == [1, 2, 2, 3, 4, 4, 6, 9, 10])
    # test to sort if it goes in ascending order if its in descending
    b = [6,5,4,3,2,1]
    mergeSortWithOneAuxList(b)
    assert(b == [1,2,3,4,5,6])
    # tests empty lists
    c = []
    mergeSortWithOneAuxList(c)
    assert(c == [])
    print("Passed.")

def testAll():
    testinvertDictionary()
    testlargestSumOfPairs()
    testcontainsPythagoreanTriple()
    testfriendsOfFriends()
    testmergeSortWithONeAuxList()
testAll()

# if __name__ == "__main__":
   # testAll()


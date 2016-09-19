import copy
def ct1(a):
    b=a
    (a,c,d) = (b + [b[0]], copy.copy(b), copy.deepcopy(b))
    d[1] = b[0]
    c[1] = d[0]
    b = b[0:1] + b[1:]
    print(a,b)
    b[0] = [3,4]
    print(a,b)
    a[0] += [5]
    c[1][0] = 1 + b[0][1]
    a[0][0] = 6 + d[1][0]
    for (s,L) in (('a',a),('b',b),('c',c),('d',d)):
        print(s,L)
a=[list(range(2-i)) for i in range(2)]
print('start:', a)
ct1(a)
print('end:',a)

print("###############")

def t3(a):
    (b,c) = (a,copy.copy(a))
    a[0] = 3
    b[0] = 4
    c[0] = 5
    print((a[0],b[0],c[0]),end="")
    a = c
    a[0] = 6
    b[0] = 7
    c[0] = 8
    print((a[0], b[0], c[0]),end="")
a = [1,2]
t3(a)
print(a[0])

print("##############")

a = [list(range(1)), list(range(2))]
(b,c) = (copy.copy(a), copy.deepcopy(a))
def ct2(a):
    try:
        a[1] = c[1]
        a[0][0] = 3
        b[0][0] = 4
        c[1][0] = 5
        c[2][0] = 6
    except:
        c[1] = 7
ct2(a)
print(a,b,c)
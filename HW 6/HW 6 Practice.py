def isLatinSquare(a):
    (rows, cols) = (len(a), len(a[0]))
    characterSet = set(a[0])
    for row in range(rows):
        rowset = set(a[row])
        if len(rowset) != len(a[row]) or rowset != characterSet:
            return False
    for col in range(cols):
        collist = []
        for row in range(rows):
            collist.append(a[row][col])
            colset = set(collist)
        if len(colset) != len(collist) or colset != characterSet:
            return False
    return True

#tr = [[1,2,3],[3,1,2],[1,2,3]]
#print(isLatinSquare(tr))

def matrixAdd(m1, m2):
    rows1 = len(m1)
    rows2 = len(m2)
    cols1 = len(m1[0])
    cols2 = len(m2[0])
    if rows1 != rows2 or cols1!= cols2:
        return None
    m3=[]
    for row in range(rows1): m3 += [[0]*cols1]

    for row in range(rows1):
        for col in range(cols1):
            m3[row][col] = m1[row][col] + m2[row][col]
    return m3

#print(matrixAdd([[1,2],[3,4]],[[3,4],[3,4]]))

def matrixMultiply(m1,m2):
    row1 = len(m1)
    row2 = len(m2)
    col1 = len(m1[0])
    col2 = len(m2[0])
    if col1 == row2:
        m3 = []
        for row in range(row1): m3 += [[0]*col2]
    elif col2 == row1:
        m3 = []
        for row in range(row2): m3 += [[0]*col1]
    rows = len(m3)
    cols = len(m3[0])
    for col in range(cols):
        collist = []
        for row in range(rows):
            collist.append()
    return 42


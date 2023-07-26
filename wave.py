from sys import stdin

def wavePrint(mat,nRows,mCols):
    #Your code goes her
    bFlag = 1
    n = nRows
    m = mCols
    j = 0
    
    while j < m:
        if bFlag == 1:
            for i in range(n):
                print(mat[i][j],end =' ')
            bFlag = 0
            j+=1
            
        else:
            for i in range(n-1, -1, -1):
                print(mat[i][j], end =' ')
            bFlag = 1
            j+=1

#Taking Iput Using Fast I/O
def take2DInput() :
    li = stdin.readline().rstrip().split(" ")
    nRows = int(li[0])
    mCols = int(li[1])
    
    if nRows == 0 :
        return list(), 0, 0
    
    mat = [list(map(int, input().strip().split(" "))) for row in range(nRows)]
    return mat, nRows, mCols


#main
t = int(stdin.readline().rstrip())

while t > 0 :

    mat, nRows, mCols = take2DInput()
    wavePrint(mat,nRows, mCols)
    print()

    t -= 1
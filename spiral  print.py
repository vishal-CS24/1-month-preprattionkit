from sys import stdin

def spiralPrint(mat, nRows, mCols):
    #Your code goes here
    m = nRows
    n = mCols
    
    k = 0; l = 0

    while (k < m and l < n) : 
        for i in range(l, n) : 
            print(mat[k][i], end = " ") 
              
        k += 1
  
        for i in range(k, m) : 
            print(mat[i][n - 1], end = " ") 
              
        n -= 1
  
        if ( k < m) : 
              
            for i in range(n - 1, (l - 1), -1) : 
                print(mat[m - 1][i], end = " ") 
              
            m -= 1
          
        if (l < n) : 
            for i in range(m - 1, k - 1, -1) : 
                print(mat[i][l], end = " ") 
              
            l += 1



























#Taking Input Using Fast I/O
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
    spiralPrint(mat, nRows, mCols)
    print()

    t -= 1
def largetRowSumAndIndex(li):
    n = len(li)
    m = len(li[0])
    
    max_sum = -2147483648
    max_index = -2147483648
    
    for i in range(n):
        sum = 0
        for j in range(m):
            sum += li[i][j]
            
        if sum > max_sum:
            max_index = i
            max_sum = sum
            
        elif sum == max_sum:
            if max_index > i:
                max_index = i
                max_sum = sum
            
    return max_index,max_sum


def largetColSumAndIndex(li):
    n = len(li)
    m = len(li[0])
    
    max_sum = -2147483648
    max_index = -2147483648
    
    for j in range(m):
        sum = 0
        for i in range(n):
            sum += li[i][j]
            
        if sum > max_sum:
            max_index = j
            max_sum = sum
            
    return max_index, max_sum

m, n=(int(i) for i in input().strip().split(' '))
l=[int(i) for i in input().strip().split(' ')]
arr = [ [ l[(j*n)+i] for i in range(n)] for j in range(m)]
row = largetRowSumAndIndex(arr)
col = largetColSumAndIndex(arr)

if row[1] > col[1]:
    print('row',end =' ')
    print(row[0],end =' ')
    print(row[1],end =' ')
    
        
elif col[1] > row[1]:
    print('column',end =' ')
    print(col[0],end =' ')
    print(col[1],end =' ')
        
else:
    print('row',end =' ')
    print(row[0],end =' ')
    print(row[1],end =' ')
    


'''# LARGEST COLUMN SUM IN A 2-D ARRAY
def lar_Col_Sum1(li):
    n = len(li) 
    m = len(li[0]) 
    max_sum = -1  
    max_sum = -1 
    for j in range(m):
        sum = 0
        for ele in li:
            sum += ele[j]
        if sum>max_sum:
            max_sum = sum
            max_index = j

    max_rindex = -1
    max_rsum = -1
    for i in range(n):
        sum = 0
        for j in range(m):
            sum += li[i][j]
        if sum > max_rsum:
            max_rsum = sum
            max_rindex = i
    if max_sum> max_rsum:
        print('column', max_index, max_sum)
    else:
        print('row', max_rindex, max_rsum)



li = [[6,9,8,5],[9,2,4,1],[8,3,9,3],[8,7,8,6]]
lar_Col_Sum1(li)'''








'''
    In order to print two or more integers in a line separated by a single 
    space then you may consider printing it with the statement, 

    print(str(num1) + " " + str(num2))
    Take Minimum value as MIN_VALUE = -2147483648

'''
'''
from sys import stdin

def findLargest(arr, nRows, mCols):
    #Your code goes here
    n = len(li) 
    m = len(li[0]) 
    max_sum = -1  
    max_sum = -1 
    for j in range(m):
        sum = 0
        for ele in li:
            sum += ele[j]
        if sum>max_sum:
            max_sum = sum
            max_index = j

    max_rindex = -1
    max_rsum = -1
    for i in range(n):
        sum = 0
        for j in range(m):
            sum += li[i][j]
        if sum > max_rsum:
            max_rsum = sum
            max_rindex = i
    if max_sum> max_rsum:
        print('column', max_index, max_sum)
    else:
        print('row', max_rindex, max_rsum)

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
    findLargest(mat, nRows, mCols)

    t -= 1'''
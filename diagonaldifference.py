def diagonalDifference(arr):
    temp,res=0,0
    n=len(arr)
    for i in range(n):
        temp+=arr[i][i]
        res+=arr[i][n-1-i]
        print(n-1-i)
    return abs(res-temp)
arr=[[12,2,3,],[1,2,3],[34,54,3]]

print( diagonalDifference(arr))
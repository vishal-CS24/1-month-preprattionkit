

def flippingMatrix(matrix):
    n=len(matrix)//2
    sum1=0
    for i in range(n):
        for j in range(n):
            sum1 += max(max(matrix[i][j],matrix[2*n-i-1][j]),max(matrix[i][2*n-j-1],matrix[2*n-i-1][2*n-j-1]))
    return sum1




# mat=[[112,142,83,119],[56,125,56,49],[15,78,101,43],[62,98,114,108]]
mat=[[1,2],[13,4]]
print(flippingMatrix(mat))
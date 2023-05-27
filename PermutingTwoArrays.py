def twoArrays(k, A, B):
    A=sorted(A)
    B=B[::-1]
    a=[0,0]
    for i in range(len(A)):
        if A[i]+B[i]<k:
            a[0] +=1
        else:
            a[1]+=1
    print(A,B)
    print(a)
    if a[0]==0:
        return "Yes"
    else:
        return 'No'
A=[2,1,3]
B=[7,8,9]
k=10
print(twoArrays(k, A, B))
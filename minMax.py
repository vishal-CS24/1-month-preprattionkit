
def maxMin(k, arr):
    # Write your code here
    arr.sort()
    min_ = arr[-1]
    for i in range(k-1,len(arr)):
        sub = arr[i] - arr[i+1-k]
        if sub < min_:
            min_ = sub
    return min_

arr=[1,2,3,3,2,5,6,5]
k=3
print(maxMin(k,arr))
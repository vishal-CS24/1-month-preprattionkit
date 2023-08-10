
def bubbleSort(arr, n):
    # Your code goes here
   # for i in range(n-1):
    for i in range(n-1):
        for j in range(0, n-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


# l = input()6546
arr = [2, 21, 12, 14, 9, 7, 5]
n = 7
# selectionsort(arr, n)
print(bubbleSort(arr, n))

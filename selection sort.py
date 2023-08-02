
from sys import stdin
def selectionsort(arr,n):
	for i in range(n-1):
		minindex=i
		for j in range(i+1,n):
			if(arr[j]<arr[minindex]):
				minindex=j
		arr[i],arr[minindex]=arr[minindex],arr[i]
	for ele in arr:
	    print(ele,end=' ')
	
def takeInput() :
    n = int(stdin.readline().strip())
    
    if n == 0 :
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n

arr, n = takeInput()
selectionsort(arr,n)

   
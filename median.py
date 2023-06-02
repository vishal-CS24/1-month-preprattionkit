def findMedian(arr):
   arr= sorted(arr)
   mid=len(arr)//2
   return arr[mid]
arr=[1,2,4,3,6,7,8,5,9]

print(findMedian(arr))
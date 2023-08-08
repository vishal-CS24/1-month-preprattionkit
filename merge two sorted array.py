from sys import stdin

def merge(arr1,arr2) : 
    #Your code goes here
     i=0
     j=0
     l1=len(arr1) 
     l2=len(arr2)
     arr3=[]
     while (i<l1 and j<l2):
            if arr1[i]<arr2[j]:
                arr3.append(arr1[i])
                i=i+1
            else :
                arr3.append(arr2[j])
                j=j+1
     while (i<l1):  
             arr3.append(arr1[i])
             i=i+1 
     while(j<l2):  
             arr3.append(arr2[j])
             j=j+1      
     return arr3

#Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().rstrip())
    if n != 0:
        arr = list(map(int, stdin.readline().rstrip().split(" ")))
        return arr, n

    return list(), 0


#to print the array/list
def printList(arr, n) : 
    for i in range(n) :
        print(arr[i], end = " ")
        
    print()


#main
t = int(stdin.readline().rstrip())

while t > 0 :

    arr1, n = takeInput()
    arr2, m = takeInput()

    ans = merge(arr1,arr2)
    printList(ans, (n + m))

    t -= 1


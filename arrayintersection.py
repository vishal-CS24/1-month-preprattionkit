
import sys

def intersections(arr1, n, arr2, m) :
    for i in range(n) : 
        for j in range(m) :
            if arr1[i] == arr2[j] : 
                print(arr1[i], end = " ")
                arr2[j] = sys.maxsize 
                break
#Taking Input Using Fast I/O
def takeInput() :
    n = int(sys.stdin.readline().strip())
    if n == 0:
        return list(), 0

    arr = list(map(int, sys.stdin.readline().strip().split(" ")))
    return arr, n
#main
t = int(sys.stdin.readline().strip())

while t > 0 :
    arr1, n = takeInput()
    arr2, m = takeInput()

    intersections(arr1, n, arr2, m)
    print()
    t -= 1





'''def printIntersection(arr1,arr2):
    output=[]
    for i in arr1:
        if(i in arr2):
            output.append(i)
    for l in output:
         print(l,end=' ')
k=1
p=int(input())
while k<=p:
 n=int(input())
 arr1=[]
 if n >0:
  arr1 = [int(x) for x in input().split()[:n]]
 m=int(input())
 arr2=[]
 if m>0:
  arr2 = [int(x) for x in input().split()[:m]]
 n1 = len(arr1)
 n2 = len(arr2)
 printIntersection(arr1, arr2)
 print()
 k=k+1'''




'''def arrayIntersection(a, b):
    ans = []
    #a.sort()
   # b.sort()
    i, j = 0, 0
    while i <len(a) and j < len(b):
        if a[i] == b[j]:
            if i == 0 or a[i - 1] != b[i-1]:b 
                ans.append(a[i])
            i += 1
            j += 1
        elif a[i] < b[j]:
            i += 1
        else:
            j += 1
    return ans
k=1
p=int(input())
while k<=p:
 m = int(input())
 arr1 = [int(x) for x in input().split()[:m]]
 n = int(input())
 arr2 = [int(x) for x in input().split()[:n]]
 res =arrayIntersection(arr1, arr2)
 for ele in res:
    print(ele,end=' ')
 print()
 k=k+1'''







'''
def printIntersection(arr1, arr2, n1, n2):
    hs = set()
    #  Insert the elements of arr1[] to set S
    for i in range(0, n1):
        hs.add(arr1[i])
    print("Intersection:")
    for i in range(0, n2):
        #  If element is present in set then
        #  push it to vector V
        if arr2[i] in hs:
            print(arr2[i], end=" ")
#  Driver Program
arr1 = [7, 1, 5, 2, 3, 6]
arr2 = [3, 8, 6, 20, 7]
n1 = len(arr1)
n2 = len(arr2)
printIntersection(arr1, arr2, n1,n2)







def arrayIntersection(a, b):
    i, j = 0, 0
    for i in str(m)and str(n):
         if m[i]==n[i]:
             return i         
k=1
p=int(input())
while k<=p:
 m = int(input())
 arr1 = [int(x) for x in input().split()[:m]]
 n = int(input())
 arr2 = [int(x) for x in input().split()[:n]]
 res =arrayIntersection(arr1, arr2)
 for ele in res:
    print(ele,end='')
 print()
 k=k+1'''


'''
def printIntersection(arr1, arr2, n1, n2):
    hs = set()
    for i in range(0, n1):
        hs.add(arr1[i])
    for i in range(0, n2):
        if arr2[i] in hs:
            print(arr2[i], end=" ")
k=1
p=int(input())
while k<=p:
 n=int(input())
 arr1 = [int(x) for x in input().split()[:n]]
 m=int(input())
 arr2 = [int(x) for x in input().split()[:m]]
 n1 = len(arr1)
 n2 = len(arr2)
 printIntersection(arr1, arr2, n1,n2)
 print()
 k=k+1

'''
'''def checkRotate(arr):
    m = min(arr)
    print(arr.index(m))
    
n=int(input())
arr = [int(x) for x in input().split()[:n]]
checkRotate(arr)'''





from sys import stdin

def arrayRotateCheck(arr, n):
    #Your code goes here
 try:
    m = min(arr)
    print(arr.index(m))
 except:
    print(0)
#Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().rstrip())
    if n == 0:
        return list(), 0

    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    return arr, n


#main
t = int(stdin.readline().rstrip())

while t > 0 :

    arr, n = takeInput()
    arrayRotateCheck(arr, n)

    t -= 1
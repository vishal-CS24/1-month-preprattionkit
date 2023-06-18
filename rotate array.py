from sys import stdin


def rotate(arr, n, d):
    #Your code goes here
 try:
    n = len(arr)
    mod = d % n 
    for i in range(n): 
        print (arr[(mod + i) % n],end = ' ')
 except:
     print('')
    

#Taking Input Using Fats I/O
def takeInput() :
    n = int(stdin.readline().rstrip())
    if n == 0:
        return list(), 0

    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    return arr, n


#to print the array/list 
def printList(arr, n) : 
    for i in range(n) :
        print(arr[i], end = " ")
    print()


#main
t = int(stdin.readline().rstrip())

while t > 0 :
    
    arr, n = takeInput()
    d = int(stdin.readline().rstrip())
    rotate(arr, n, d)
    print()
    #printList(arr, n)
    
    t -= 1
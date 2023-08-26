def sort(ar):
    a = 0
    b = 0
    c = 0
    for i in ar:
        if i == 0:
            a+=1
        elif i==1:
            b+=1
        else:
            c+=1
    res = []
    for i in range(0, a):
        res.append(0)
    for i in range(0, b):
        res.append(1)
    for i in range(0, c):
        res.append(2)
        
    for i in res:
        print(i, end = ' ')
k=1
p=int(input())
while k<=p:
 n = int(input())
 ar = [int(x) for x in input().split()[:n]]
 sort(ar)
 print()
 k=k+1
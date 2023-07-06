
def rev(li, l):
    res = li[0]
    for i in range(1, l):
        res = res ^ li[i]
    return res
k=1
p=int(input())
while k<=p:
 n = int(input())
 li = [int(x) for x in input().split()[:n]]
 print(rev(li, len(li)))
 print()
 k=k+1









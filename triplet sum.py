def pairSum(ar, n, x):
    count=0
    for i in range(n):
        for j in range(i+1,n):
            for m in range (j+1,n):
               if ar[i]+ar[j]+ar[m] == x:  
                 count=count+1
    print(count)  
k=1
p=int(input())
while k<=p:       
 n = int(input())
 ar=[]
 if n>0:
  ar = [int(x) for x in input().split()[:n]]
 x = int(input())
 pairSum(ar, n, x)
 k=k+1
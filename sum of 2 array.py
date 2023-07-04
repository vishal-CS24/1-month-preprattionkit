
'''def calSumUtil( a , b , n , m ):
    # array to store sum.
    sum = [0] * n
    i = n - 1
    j = m - 1
    k = n - 1
     
    carry = 0
    s = 0
     
    while j >= 0:

        s = a[i] + b[j] + carry
        sum[k] = (s % 10)
         
        carry = s // 10
         
        k-=1
        i-=1
        j-=1
     
    while i >= 0:
 
        s = a[i] + carry
        sum[k] = (s % 10)
        carry = s // 10
         
        i-=1
        k-=1
     
    ans = 0

    if carry:
        ans = 10
     
    for i in range(n):
        ans += sum[i]
        ans *= 10
     
    return ans // 10
 
def calSum(a, b, n, m ):
 
    if n >= m:
        return calSumUtil(a, b, n, m)
    else:
        return calSumUtil(b, a, m, n)
 
p=int(input())
while p>0:
 n = int(input())
 a = [int(x) for x in input().split()[:n]]
 m = int(input())
 b = [int(x) for x in input().split()[:m]]
 ans=[]
 ans= str(calSum(a, b, n, m))
 for i in ans:
  print(i,end=' ')
 p-=1'''






from sys import stdin

def calSumUtil(a, b, n, m) :
    #Your code goes here
    sum = [0] * n
    i = n - 1
    j = m - 1
    k = n - 1
     
    carry = 0
    s = 0
     
    while j >= 0:

        s = a[i] + b[j] + carry
        sum[k] = (s % 10)
         
        carry = s // 10
         
        k-=1
        i-=1
        j-=1
     
    while i >= 0:
 
        s = a[i] + carry
        sum[k] = (s % 10)
        carry = s // 10
         
        i-=1
        k-=1
     
    ans = 0

    if carry:
        ans = 10
     
    for i in range(n):
        ans += sum[i]
        ans *= 10
     
    return ans // 10
 
def calSum(a, b, n, m ):
 
    if n >= m:
        return calSumUtil(a, b, n, m)
    else:
        return calSumUtil(b, a, m, n)

#main
t = int(stdin.readline().rstrip())

while t > 0 :
 n = int(input())
 a=[]
 if n>0:
  a = [int(x) for x in input().split()[:n]]
 m = int(input())
 b=[]
 if m>0:
  b = [int(x) for x in input().split()[:m]]
 ans=[]
 ans= str(calSum(a, b, n, m))
 for i in ans:
  print(i,end=' ')
    
 t -= 1
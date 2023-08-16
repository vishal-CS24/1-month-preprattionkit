'''
55555
4444
333
22
1

n=int(input())
i=1
while i<=n:
	j=1
	while j<=n-i+1:
	      print(n-i+1,end="")	
	      j=j+1	      
	print()
	i=i+1
#or

n=int(input())
i=1
while i<=n:
	j=n
	while j>=i:
	      print(n-i+1,end="")	
	      j=j-1	      
	print()
	i=i+1'''


#4th
"""A
BB
CCC
DDDD
EEEEE


n=int(input())
i=1
while i<=n:
	j=1
	while j<=i:
	      print(chr(ord('A')+i-1),end="")	
	      j=j+1	      
	print()
	i=i+1"""


"""#3rd
12345
1234
123
12
1


n=int(input())
i=1
while i<=n:
	j=n
	while j>=i:
	      print(n-j+1,end="")	
	      j=j-1	      
	print()
	i=i+1"""


'''#ist
1
11
202
3003
40004

n = int(input())
i=1
while i<=n:
    j=0
    while j<i:
        if i==1:
            print(1, end="")
        elif j and j<i-1:
            print(0, end="")
        else:
            print(i-1, end='')
        j=j+1
    print()
    i=i+1'''

#2nd
'''
1
11
121
1221
12221


n = int(input())
i=1
while i<=n:
    j=0
    while j<i:
        if i==1:
            print(1, end="")
        elif j and j<i-1:
            print(2, end="")
        else:
            print(1, end='')
        j=j+1
    print()
    i=i+1'''

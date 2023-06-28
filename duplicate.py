'''# Python program to print
# duplicates from a list
# of integers
def Repeat(x):
	_size = len(x)
	repeated = []
	for i in range(_size):
		k = i + 1
		for j in range(k, _size):
			if x[i] == x[j] and x[i] not in repeated:
				repeated.append(x[i])
	return repeated

# Driver Code
n=int(input())
list1 =  [int(x) for x in input().split()]
print (Repeat(list1))
	
# This code is contributed
# by Sandeep_anand'''

def Repeat(x):
	_size = len(x)
	repeated = []
	for i in range(_size):
		k = i + 1
		for j in range(k, _size):
			if x[i] == x[j] and x[i] not in repeated:
				repeated.append(x[i])
	return repeated
r=1
p=int(input())
while r<=p:
 n=int(input())
 list1 =  [int(x) for x in input().split()]
 #rl=Repeat(list1)
 for rl in Repeat(list1):
     print(rl)
 r=r+1

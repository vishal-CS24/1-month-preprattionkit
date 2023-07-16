def checkPermutation(a, b):
    li_1 = sorted(a)
    li_2 = sorted(b)
    
    size = len(li_1)
    
    for i in range(size):
        if li_1[i] != li_2[i]:
            print('false')
            break
            
    else:
        print('true')
        
a = input()
b = input()

checkPermutation(a, b)




'''
      OR
from sys import stdin
def checkPermutation(a, b):
    li_1 = sorted(a)
    li_2 = sorted(b)
    
    size = len(li_1)
    
    for i in range(size):
        if li_1[i] != li_2[i]:
            return 'false'
            break
    else:
         return 'true'
        
a = stdin.readline().strip()
b = stdin.readline().strip()

print(checkPermutation(a, b))'''


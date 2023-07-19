import itertools
def removeConsecutiveDuplicates(s):
     return (''.join(i for i, _ in itertools.groupby(s)))
    
    
s= input()
print(removeConsecutiveDuplicates(s))
def birthday(s, d, m):#s is array of interger on each square , d is date of birth and m is month of birth
    i=0
    j=m
    c=0
    while j<=len(s):
        if sum(s[i:j])==d:
            c+=1
        i+=1
        j+=1
    return c
s=[2,3,4,2,12,2,2]
d=4
m=2
print(birthday(s, d, m))
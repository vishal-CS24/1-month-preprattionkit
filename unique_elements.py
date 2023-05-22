def lonelyinteger(a):
    for i in a:
        if a.count(i)==1:
            return i
print(lonelyinteger([1,1,2,3,4,2,3,4,5,6,6]))
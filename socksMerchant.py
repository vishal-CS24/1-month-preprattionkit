#find number of pairs of socks having same color
def sockMerchant(ar):
    li={}
    for i in ar:
        c=ar.count(i)//2
        if i in li:
            pass
        else:            
            li[i]=c
    return sum(li.values())

print(sockMerchant([1,1,2,3,4,5,4,3,2,3,2,1,2,3,3,43,2,1,2,3]))
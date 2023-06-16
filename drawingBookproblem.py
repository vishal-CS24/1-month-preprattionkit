def pageCount(n, p):
    #p//2 gives the total flips till page p form start
    # n//2-p//2 gives us the total flips form end and then we find min of then that is our answer
    return min(p//2,n//2-p//2)

n=9 #Total number of pages
p=4 #page at which we have to go

print(pageCount(n,p))
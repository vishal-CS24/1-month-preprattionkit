
#print unsigned integer
def flippingBits(n):
    return ~n+2**32

print(flippingBits(10))
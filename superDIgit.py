#method 1 

def superDigit(n, k):
    a=sum(int(i) for i in n)
    b=str(a*k)
    if len(b)==1:
        return b
    else:
        return superDigit(b,1)

# method 2
def superDigit1(n, k):
    n_str = str(n)
    n_sum = sum(int(x) for x in n_str)
    n_sum *= k
    
    digital_root = 1 + ((n_sum - 1) % 9)
    return digital_root

n='2342352'
k=1
print("Answer with ist method : ",superDigit(n,k))
print("Answer with 2nd method",superDigit1(n,k))
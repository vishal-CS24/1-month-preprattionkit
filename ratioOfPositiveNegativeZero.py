def plusMinus(arr):
    s=len(arr)
    p=0
    n=0
    z=0
    for i in arr:
        if i<0:
            n+=1
        elif i>0:
            p+=1
        else:
            z+=1
    print(f"{p/s:.6f}")
    print(f"{n/s:.6f}")
    print(f"{z/s:.6f}")

arr=[1,2,0,-1,-2,-3,4,0,45,0,4]
plusMinus(arr)
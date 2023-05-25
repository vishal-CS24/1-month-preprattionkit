def countingSort(arr):
    ans=[0 for i in range(101)]
    for i in arr:
        ans[i]+=1
    return ans




a=[1,1,3,2,1,3,7,8,6]

anss=countingSort(a)
fans=[]
for i in anss:
    if i!=0:
        for j in range(i):
            print(anss.index(i),end=' ')
# print(anss)
# print(fans)

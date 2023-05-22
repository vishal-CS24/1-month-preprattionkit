import sys
# def miniMaxSum(arr):
#     max1= -100
#     min1 = sys.maxsize
    
#     for i in arr:
#         sum1=0
#         for j in arr:
#             if j==i:
#                 pass
#             else:
#                 sum1+=j
#         if max1<sum1:
#             max1=sum1
#         if min1>sum1:
#             min1=sum1
#     print(min1,max1)
def miniMaxSum(arr):
    sums=[sum(arr)-ele for ele in arr]       
    print(min(sums),max(sums))

arr=[1,2,3,4,5]
miniMaxSum(arr)
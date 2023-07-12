def reverseEachWord(str):
    li = str.split(' ')
    size = len(li)

    for i in range(size):
        s = li[i]
        oSize = len(s)
        for j in range(oSize-1, -1,-1):
            print(s[j],end ='')
        print('', end =' ')
        
str = input()
reverseEachWord(str)
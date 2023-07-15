def stringCompression(s):
    i = 0
    res = []
    while i < len(s) :
        j = i + 1
        c = 1
        while j < len(s):
            if s[i] == s[j]:
                c+=1
                j+=1
                
            else:
                break
            
        if c > 1:
            res.append(s[i])
            res.append(c)
            
        else:
            res.append(s[i])
            
        i = i + c
                
    for i in range(len(res)):
        print(res[i],end ='')
           

s = input()
stringCompression(s)
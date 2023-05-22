def matchingStrings(strings, queries):
    result=[]
    for i in queries:
        result.append(strings.count(i))
    return result
strings=[1,2,3,4,5,5,4,3,2,3,4,5,5]
queries=[1,2,3,4,5]
print(matchingStrings(strings, queries))
# ASCII_SIZE = 256


# def highestOccuring(s):
#     count = [0] * ASCII_SIZE
#     max = -1
#     c = ''
#     for i in s:
#         count[ord(i)] += 1

#     for i in s:
#         if max < count[ord(i)]:
#             max = count[ord(i)]
#             c = i

#     return c


ASCII_SIZE = 256


def highestOccuring(s):
    count = [0]*ASCII_SIZE
    max = -1
    ans = ''
    for i in s:
        count[ord(i)] += 1
        if max < count[ord(i)]:
            max = count[ord(i)]
            ans = i
    return ans


s = input()
print(highestOccuring(s))


'''from sys import stdin


def removeAllOccurrencesOfChar(string, ch) :
	# Your code goes here
   for i in range(len(string)):
      if string[i]==ch:
          print('',end='')
      else:
         print(string[i],end='')
#main
string = stdin.readline().strip()
ch = stdin.readline().strip()[0]
removeAllOccurrencesOfChar(string, ch)

          OR

'''
   


from sys import stdin


def removeAllOccurrencesOfChar(string, ch) :
	# Your code goes here
   r=string.replace(ch,'')
   return r
#main
string = stdin.readline().strip()
ch = stdin.readline().strip()[0]
ans=removeAllOccurrencesOfChar(string, ch)
print(ans)


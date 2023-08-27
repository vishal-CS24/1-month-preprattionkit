#pre functions
a=[23,45,67,87,89,90,45]


print(abs(-90))
print(abs(42))
print(max([1,6,7,0,4,7,1,5,10]))
print(min([1,6,7,0,4,7,1,5,10]))
print(sum([1,6,7,0,100,4,7,1,5,10]))




#modules
#import datetime
#help('modules')
#time
from datetime import time
t=time(10,50,59)#time
print(t)
#date
from datetime import date
d=date.today()
print(d)
#calendar
import calendar
y=int(input("enter year "))
m=int(input("enter month "))
c=calendar.month(y,m,7,2)#year,month,width,height
print(c)
#print(calendar.calendar(y,m)) ---for full calendar
#import math functions
from math import sqrt,pi,cos
radius=int(input("enter radius of circle : "))
area=2*pi*radius**2
print("area of circle is : ",area)

s=sqrt(radius)
print("sqrt of ",radius," is ",s)
c=cos(0)
print(c)
#dice
import random
for i in range(1):
	value=random.randint(1,6)
	print(value)

#functioons as objects
def add(x,y):
	return x+y
def twice(fun,x,y):
	return fun(fun(x,y),fun(x,y))
a=5
b=5
print(twice(add,a,b))


def math(x,y):
	return x+y
a=input("enter a ")
b=input("enter b ")
print(math(a,b))


#function with arguments
def numbers(x,y):
	"""this is docstring comment"""
	sum=x+y
	return sum
	print("hello")
n=numbers(100,45)
print("sum = ",n)


#0th
def ret(x,y):
 if x>y:
  return x
 else:
  return y
print(ret(4,3))
z=ret(8,9)
print(z)

# ist

def area(len,bre):
	ar=len*bre
	pr=2*(len+bre)
	#print("area = ",ar)
	print("perimeter = ",pr)
area(int (input("enter length : ")),int (input("enter breadth ")))

#2nd
def password(p1,p2):
	if(p1==p2):
		print("Both passwords are same")
		print()
	else:
		print("Both passwords are different")

password(input("enter password : "),input("re-enter password "))
		
#3rd
def func(x):
	print(x)
func("Hello,this is vishal")
func(100000)
	
#functions are declaired by def
def welcome_message():
	#redesign this function
	name = input()
	print("Welcome,",name )
welcome_message()




def check():
         print("this is vishu")
check()       
	
	
	
#project
a = int(input("enter ist value "))
b = int(input("enter 2nd value "))
c=list(range(a,b))
print (c)





n = int(input())
for x in range(1, n):
    if x%2==0:
     continue 
    if x % 3 == 0 and x % 5 == 0:
        print("SoloLearn")
    elif x % 3 == 0:
        print("Solo")
    elif x % 5 == 0:
        print("Learn")
    else:
        print(x)


#for + range
for i in range(4):
	print("Hello this is vishu")


#range

num=list(range(1,20,4))# 1 =starting,20=end,2=gap/step
print(num)




num=list(range(2,10))
print(num)
print(len(num))


print(range(10))==range(0,10)

num=list(range(10))
print(num)




#for loop
list=[2,3,4,5,6,7]
for x in list:
	if(x%2==1 and x>4):
		print(x)
	


str="This is vishal gupta"
count=0
for x in str:
	if(x=='i'):
		count+=1
		print(count)
		continue
		
	         
                     


words=["hello","vishu","good","Amit","sudhanshu"]
for word in words:
	print(word + "!")




#while loop
i=0
while i<5:
	i+=1
	if i==3:
		print("skipping 3")
		continue
	
#code
i=1
sum=0
while i<=10:
        sum+=i 
        i+=1
        print("sum=",sum)
        
       

#ist
i=1
while i<=5:
	if i%2==0:
		print(i," is even")
	else:
		print(i," is odd")
	i+=1
	
#2nd
i=1
while i<=5:
 print(i,"This is vishal")
 i+=1
	

#index
word=["this ","is","vishal"]
l=word.index("vishal")
print(l)
a=[23,34,45,67,78]
a.append(79)#add at end
a.insert(5,100)#insert
print(a)
b=a.index(79)#loc of 79
print(b)

#append function and len function , insert
nums=[1,2,3,4,5]
nums.append(16)
nums.append(17)
nums.append(18)
print(nums)
a=len(nums)#length
print(a)
#insert
index=0
nums.insert(index,'hello this is inserted at 1st index')
print(nums)

#searching is lists
st="This is vishal gupta"

if "gup" in st:
  print( "yes")
print(len(st))

words=["happy","sad","angry","apple","banana"]
print("happy" in words)#true because happy is in list
print("vishu" in words)#False because vishu is not in list
print("vishu" not in words)#true
print(not "sad" in words)#false bacause item is present


#lists
nums=[7,4,5]
print(nums+[3,6,8])
print(nums*3)


value=[
      [11,22,33],
      [23,34,45],
      [12,24,36]
    ]
print(value[0][2])
print(value[0][1])
print(value[0][0])
#replacement
value[2][2]=5
print(value[2])

items=["hello","vishu",831,["love","you",971],431]
print(items[3][0],items[1],items[4])

mpty_list=[]
print(mpty_list)

#and or operators
len=int(input("enter length : "))
bre=int(input("enter Breadth : "))
hei=int(input("enter Height : "))
if len+bre==hei or len+hei==bre or bre+hei==len:
	print("you are allowed to use pythagorous")
else:
	print("You are not allowed")
	

#if,else,elif statements

len=int(input("enter length : "))
bre=int(input("enter Breadth : "))
hei=int(input("enter Height : "))
if len+bre==hei:
	print("you are allowed to use pythagorous")
elif len+hei==bre:
	print("You are not allowed to use theoram")
elif bre+hei==len:
	print("You are not allowed to use theoram")
else:
	print("You are not allowed")





age=int(input("enter your age : "))
if age>=18:
	print("you are allowed")
else:
	print("You are not allowed")


temp=int(input("enter temperature : "))
if temp>100:
 print("Water is boiling")
else:
 print("water is not boiling")

    
print(78>=79)
a=10
b=20
b+=a
print("sum is",b)

#concatination
name= input('enter name ')
age= int(input("enter age "))
print("hello "+name + " your age is " + str(age))

srname=input("enter your sirname : ")
print(name +" "+srname)


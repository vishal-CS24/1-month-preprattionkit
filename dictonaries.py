#To determine whether a key is in a dictionary, you can use in and not in, just as you can for a list.
nums={
1:"one",
2:"two",
3:"three",
4:"apple",
"abc":[8,9,10]
}
print(1 in nums)
print("two" in nums)
print(4 not in nums)
print(nums.get(1,0))
print(nums.get("abc"))
print(nums.get(0,"not in dictionary\n"))
print(nums.get(0,"not in dictionary\n"))

#to dd values in dictionry
sq={1:1,2:4,3:10,4:16}
sq[8]=64
sq[3]=9#it replace the value
print(sq)


#create a distionary details and use of exception handling
try:
 details ={ "Name": "Vishal",  
 "class": "Btech",
 "rollno": 2028230
 }
 print(details["Name"])
 print(details["rollno"])
 print(details["v"])
except:
	print("something went wrong")
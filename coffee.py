coffee = ["Café Latte", "Caffe Americano", "Espresso", "Cappuccino", "Macchiato"]
choice = int(input("please enter a number for coffee : "))
l=len(coffee)
try:
	choice < l
	print("your selected coffee is : "+coffee[choice])
except:
	print("Please enter a number between 0 and 4")
finally:
	print("Have a good day!")
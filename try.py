try:
	x = int(input("Enter a number: "))
	y = 1 / x
	print(y)
except ZeroDivisionError as excl1:
	print("You cannot divide by zero, sorry.")
except ValueError as excl2:
	print("You must enter an integer value.")
except:
	print("Oh dear, something went wrong...")
print("THE END.")
    
# Python program to check if
# given number is prime or not

# Method 1
num = int(input("Enter a number : "))

# If given number is greater than 1
if num > 1:

	# Iterate from 2 to n / 2
	for i in range(2, num//2 + 1):

		# If num is divisible by any number between
		# 2 and n / 2, it is not prime
		if (num % i) == 0:
			print(num, "is not a prime number")
			break
	else:
		print(num, "is a prime number")

else:
	print(num, "is not a prime number")

# method 2

from math import sqrt
n = 1

prime_flag = 0

if(n > 1):
	for i in range(2, int(sqrt(n)) + 1):
		if (n % i == 0):
			prime_flag = 1
			break
	if (prime_flag == 0):
		print("true")
	else:
		print("false")
else:
	print("false")
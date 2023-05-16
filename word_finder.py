
# Given two strings: one being a word (e.g., "cat") and the second being a combination of any characters.

# The program attempts to answer the following question: 
#   Are the characters comprising the first string hidden inside the second string?

word = input("Enter the word you wish to find: ").upper()
strn = input("Enter the string you wish to search through: ").upper()

found = True
start = 0

for ch in word:
	pos = strn.find(ch, start) 
	if pos < 0:
		found = False
		break
	start = pos + 1
if found:
	print("Yes")
else:
	print("No")
	


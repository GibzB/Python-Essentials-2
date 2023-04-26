# rfind() method
# The rfind() method returns the highest index of the substring (if found). If not found, it returns -1.
# The one-, two-, and three-parameter versions of the rfind() method do nearly the same things as their counterparts (the ones devoid of the r prefix), 
#   NOTE
#       but start their searches from the END of the string, (hence the prefix r, for right).

# Demonstrating the rfind() method:
print("tau tau tau".rfind("ta")) # This line searches the entire string for the last occurrence of "ta" and returns its index.
print("tau tau tau".rfind("ta", 9)) # This line starts searching the string from the index position 9 (inclusive) and searches backwards for the last occurrence of "ta,
# , since there are no occurrences of "ta" after index position 9, the method returns -1 as the output.
print("tau tau tau".rfind("ta", 3, 9)) # This line searches the substring between index positions 3 and 9 (inclusive) for the last occurrence of "ta". 
#   Since the last occurrence of "ta" in this substring is at index position 4, the output is 4

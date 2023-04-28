# strip() method

# The strip() method combines the effects caused by rstrip() and lstrip() 
#   – it makes a new string lacking all the leading and trailing whitespaces.

# The strip() method has one more interesting feature: it can remove a substring from the beginning and the end of a string.

# Its syntax is as follows: string.strip(substring)

# The method will look for the substring in the string, and if it finds it,
#   it will remove it from the string.

# If it doesn't find the substring, it will do nothing.
# Demonstrating the strip() method:
print("[" + "   aleph   ".strip() + "]") # there is space character in the aleph string, before and after


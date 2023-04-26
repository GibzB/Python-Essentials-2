# lstrip() method
# The lstrip() method returns a copy of the string with the leading characters removed (based on the string argument passed).

# The parameterless version of the lstrip() method returns a newly created string formed from the original one by removing all leading whitespaces.

# Demonstrating the lstrip() method:
print("[" + " tau ".lstrip() + "]") # there is a space before the start of tau


# The one-parameter version of the lstrip() method removes all characters included in the argument (a string), not just whitespaces:

# Demonstrating the lstrip() method:
print("www.cisco.com".lstrip("w.")) # prints out characters AFTER(Leading) w. 
# replace() method
# The replace() method returns a copy of the string where all occurrences of a substring is replaced with another substring.
# The replace() method takes two parameters:
#   1. old – the substring you want to replace
#   2. new – the substring you want to replace old with

# The replace() method returns a copy of the string where all occurrences of old are replaced with new.
# The replace() method doesn't modify the original string.
# The replace() method takes three parameters:
#   1. old – the substring you want to replace
#   2. new – the substring you want to replace old with
#   3. count – the number of times you want to replace old with new

# The replace() method returns a copy of the string where the first count occurrences of old are replaced with new.
# The replace() method doesn't modify the original string.

# Demonstrating the replace() method:
# Two parameters
print("www.netacad.com".replace("netacad.com", "pythoninstitute.org"))
print("This is it!".replace("is", "are"))
print("Apple juice".replace("juice", ""))

# Three parameters
print("This is it!".replace("is", "are", 1))
print("This is it!".replace("is", "are", 2))
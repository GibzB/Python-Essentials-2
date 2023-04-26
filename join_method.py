# join() method

# The join() method is a string method and returns a string in which the elements of sequence have been joined by str separator.
# the method performs a join – it expects one argument as a list; 
#   it must be assured that all the list's elements are strings – the method will raise a TypeError exception otherwise;
#   all the list's elements will be joined into one string but...
#   ...the string from which the method has been invoked is used as a separator, put among the strings;
#   the newly created string is returned as a result

# The join() method is called on a string, gets the string you want to join with the string as an argument,
# and returns a new string consisting of the two strings joined together.

# The join() method provides a flexible way to create strings from iterable objects.
# It joins each element of an iterable (such as list, string, and tuple) by a string separator (the string on which the join() method is called) and returns the concatenated string.

# Demonstrating the join() method:
print(",".join(["omicron", "pi", "rho"]))


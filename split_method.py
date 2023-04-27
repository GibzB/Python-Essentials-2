# split method

# It splits the string and builds a list of all detected substrings.

# The method assumes that the substrings are delimited by whitespaces 
#   – the spaces don't take part in the operation, and aren't copied into the resulting list.

#   If the string is empty, the resulting list is empty too.
# The split() method returns a list of substrings separated by a delimiter.
# The split() method takes maximum of 2 parameters:
    # separator (optional)- The is a delimiter. The string splits at the specified separator.
    # maxsplit (optional) - The maxsplit defines the maximum number of splits.
# If the maxsplit value is specified, the list will have the maximum of maxsplit+1 items.

# Demonstrating the split() method:
print("string1       stri\nng1".split())
print("string1       stri\nng1".split(' '))
print("string1       stri\nng1".split('\n')) 
print("phi       chi\npsi".split('i'))
print("phi       chi\npsi".split('s'))
print("phi       chi\npsi".split())

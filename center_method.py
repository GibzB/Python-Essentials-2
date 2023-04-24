# the center() method makes a copy of the original string, trying to center it inside a field of a specified width.
# The centering is actually done by adding some spaces before and after the string.

# The center() method takes two arguments:
# # the first argument is the width of the field;
# # the second argument is the character that will be used to fill the empty space in the field.
#       The two-parameter variant of center() makes use of the character from the second argument, instead of a space.

print('[' + 'gamma'.center(20, '*') + ']')



# The center() method returns a new string, so it doesn’t modify the original string.
# It’s important to remember that the center() method doesn’t modify the original string, but it returns a new string.

# The center() method is a string method, so it can be used only on strings.

# Demonstrating the center() method:
print('[' + 'alpha'.center(10) + ']')
print('[' + 'Beta'.center(2) + ']')
print('[' + 'Beta'.center(4) + ']')
print('[' + 'Beta'.center(6) + ']')



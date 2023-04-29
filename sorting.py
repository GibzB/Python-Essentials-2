# SORTING
# sorting is in fact a very sophisticated case of comparing

# SORTING STRINGS
# sorting strings is a bit more complicated than sorting numbers
# the reason is that strings are sequences of characters

# The function takes one argument (a list) and returns a new list, filled with the sorted argument's elements.

# Demonstrating the sorted() function:
first_greek = ['omega', 'alpha', 'pi', 'gamma']
first_greek_2 = sorted(first_greek)

print(first_greek)
print(first_greek_2)

print()


# The second method affects the list itself – no new list is created. 
# Ordering is performed in situ by the method named sort().

# Demonstrating the sort() method:
second_greek = ['omega', 'alpha', 'pi', 'gamma']
print(second_greek)

second_greek.sort()
print(second_greek)
# The find() method returns the index of the first occurrence of the substring in the string.
# If the substring is not found, it returns -1.

# Demonstrating the find() method:
print("Eta".find("ta"))
print("Eta".find("mma"))


t = 'theta'
print(t.find('eta'))
print(t.find('et'))
print(t.find('the'))
print(t.find('ha'))

# The first find() call t.find('eta') searches for the substring "eta" in the string "theta". 
# Since "eta" appears in "theta" starting at index 2, the find() method returns 2 as the output.

# The second find() call t.find('et') also searches for the substring "et" in the string "theta". 
# Since "et" appears in "theta" starting at index 2, the find() method again returns 2 as the output.

# The third find() call t.find('the') searches for the substring "the" in the string "theta". 
# Since "the" appears at the beginning of "theta", the find() method returns 0 as the output.

# The fourth find() call t.find('ha') searches for the substring "ha" in the string "theta". 
# Since "ha" does not appear in "theta", the find() method returns -1 as the output.


# finding from any postion:
# you can use a two-parameter variant of the find() method.
# The second argument specifies the index at which the search will be started (it doesn't have to fit inside the string).
print('\n', 'Two arguements: ')
print('kappanga'.find('a', 2))


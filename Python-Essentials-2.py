# Modules
# 

import math
print(math.sin(math.pi/2))

# Note: 
# No other entities are imported. Moreover, you cannot import additional entities using a qualification - a line like this one:

print(math.e) # will cause an error (e is Euler's number: 2.71828...)

# Fixed as below
from math import sin, pi

print(sin(pi/2))

# Importing a module
# The asterisk (*) is called a wildcard. It is used to indicate that all entities from the indicated module are imported.
# the name of an entity (or the list of entities' names) is replaced with a single asterisk (*).
# The asterix indicates ==> imports all entities from the indicated module

from module import *



# The AS keyword

# The AS keyword is used to alias a module.
# If you use the import module variant and you don't like a particular module's name 
#   (e.g., it's the same as one of your already defined entities, so qualification becomes troublesome) you can give it any name you like - this is called aliasing.
# Aliasing causes the module to be identified under a different name than the original.

import module as alias

# execution of an aliased import, the original module name becomes inaccessible and must not be used.

# In turn, when you use the from module import name variant and you need to change the entity's name, you make an alias for the entity. This will cause the name to be replaced by the alias you choose.

# This is how it can be done:

from module import name as alias
 
# The phrase name as alias can be repeated - use commas to separate the multiplied phrases, like this:

from module import n as a, m as b, o as c

# Standard Modules
# The Python Standard Library is a set of modules that comes with Python.

# dir() function
# The dir() function returns a list of all entities defined in a module.
# There is one condition: the module has to have been previously imported as a whole


# Note: if the module's name has been aliased, you must use the alias, not the original name.

dir(module)
dir(alias)

# Randomness in computers
# Computers are deterministic machines. They always perform the same operations on the same data, and they always produce the same results.
# The random module is used to generate random numbers.

# The seed function
# The seed function is used to initialize the random number generator.




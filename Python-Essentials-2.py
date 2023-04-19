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


# The randrange and randint functions
# The randrange function returns a random integer from the range specified by the user.
from random import randrange, randint

randrange(end)
randrange(beg, end)
randrange(beg, end, step)

from random import randrange, randint

print(randrange(1), end=' ')
print(randrange(0, 1), end=' ')
print(randrange(0, 1, 1), end=' ')
print(randint(0, 1))

# they may produce repeating values even if the number of subsequent invocations is not greater than the width of the specified range.

# The randint function returns a random integer from the range specified by the user.
from random import randint

for i in range(10):
    print(randint(1, 10), end=',')

#  choice and sample functions
from random import choice, sample

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(choice(my_list))
print(sample(my_list, 5))
print(sample(my_list, 10))


# The Platform function
# The platform function returns the name of the operating system on which the program is running.
# The platform module lets you access the underlying platform's data, i.e., hardware, operating system, and interpreter version information.

# The platform function returns a string containing the name of the operating system on which the program is running.
# The platform function can be invoked in two ways:
#   platform() - returns the name of the operating system on which the program is running
#   platform(aliased, terse) - returns a string containing the name of the operating system on which the program is running,
#       the version of the operating system, the machine type, and the processor type.

import platform
platform(aliased = False, terse = False)
# aliased → when set to True (or any non-zero value) it may cause the function to present the alternative underlying layer names instead of the common ones;
# terse → when set to True (or any non-zero value) it may cause the function to present the information in a terse form.


# The MACHINE function
# The machine function returns the machine type on which the program is running.
# The machine function can be invoked in two ways:
#   machine() - returns the machine type on which the program is running
#   machine(aliased, terse) - returns a string containing the machine type on which the program is running,
#       the version of the machine, the machine type, and the processor type.

from platform import machine

print(machine())


# The PROCESSOR function
# The processor function returns the processor type on which the program is running.

from platform import processor

print(processor())

# The system function
# A function named system() returns the generic OS name as a string.

from platform import system

print(system())

# The version function
# The OS version is provided as a string by the version() function.

from platform import version

print(version())

# The python_implementation and the python_version_tuple functions
# The python_implementation function returns the name of the Python implementation as a string.
# The python_version_tuple function returns the Python version as a tuple of strings.

from platform import python_implementation, python_version_tuple

print(python_implementation())
print(python_version_tuple())

# Python Module Index
# The Python Module Index is a searchable list of all available modules in the Python Standard Library.
# The Python Module Index is available at https://docs.python.org/3/py-modindex.html


# PACKAGES
# Packages are a way of structuring Python's module namespace by using "dotted module names".

# Module Search
# When a module named spam is imported, the interpreter first searches for a built-in module with that name.
# If not found, it then searches for a file named spam.py in a list of directories given by the variable sys.path.
# sys.path is initialized from these locations:

# the folder in which the execution starts is listed in the first path's element.

# to tell your module's user that a particular entity should be treated as private (i.e. not to be explicitly used outside the module) 
# you can mark its name with either the _ or __ prefix
#   (the latter is called a double underscore). This is called name mangling.

# If you want convince Python that it should take into account a non-standard package's directory, 
# its name needs to be inserted/appended into/to the import directory list stored in the path variable contained in the sys module.

# A Python file named __init__.py is implicitly run when a package containing it is subject to import, and is used to initialize a package and/or its sub-packages (if any). 
# The file may be empty, but must not be absent.


# Question 1: 
# You want to prevent your module's user from running your code as an ordinary script. How will you achieve such an effect?
import sys

if __name__ == "__main__":
    print ("Don't do that!")
    sys.exit()
    
# Question 2:
# Some additional and necessary packages are stored inside the D:\Python\Project\Modules directory. 
# Write a code ensuring that the directory is traversed by Python in order to find all requested modules.
import sys

# note the double backslashes!
sys.path.append("D:\\Python\\Project\\Modules")

# Question 3:
# The directory mentioned in the previous exercise contains a sub-tree of the following structure:

# abc
# |__ def
#     |__ mymodule.py
# Assuming that D:\Python\Project\Modules has been successfully appended to the sys.path list, 
# write an import directive letting you use all the mymodule entities.

# >> import abc.def.mymodule

# Python Package Installer (PIP)
# The Python Package Installer (PIP) is a tool for installing and managing Python packages.

# The pip command
# The pip command is used to install and manage Python packages.
# The pip command is available in the command prompt.

#PyPI
# PyPI is the Python Package Index, a repository of software for the Python programming language.
# and it's maintained by a workgroup named the Packaging Working Group, a part of the Python Software Foundation, 
#  whose main task is to support Python developers in efficient code dissemination.

# PyPI is available at https://pypi.org/


# DEPENDANCIES
# A dependency is a package that is required by another package to work properly.

# you want to know what Python packages have been installed so far, you can use the list operation
# >> pip3 list

# to tell you more about any of the installed packages
# >> pip show package_name

# to convince pip to confess something about itself.
# >> pip show pip

# To distinguish between these two actions, pip uses a dedicated option named --user
# If you don’t add this, pip assumes that you’re a system administrator and it’ll do nothing to correct you if you’re not.

# CHARACTERS & STRINGS
# A string is a sequence of characters.
# A character is a symbol that represents a letter, a number, or a punctuation mark.

# I18N (internationalization)
# I18N is the process of designing a software application so that it can potentially be adapted to various languages and regions without engineering changes.

# L10N (localization)
# L10N is the process of adapting a software application to a specific region or language.

# Code Point
# A code point is a number that represents a character.
#   e.g, 32 is a code point which makes a space in ASCII encoding.

# Unicode
# Unicode is a computing industry standard for the consistent encoding, representation, and handling of text expressed in most of the world's writing systems.
#   Unicode assigns unique (unambiguous) characters (letters, hyphens, ideograms, etc.) to more than a million code points
#   Unicode is a superset of ASCII, which is a subset of Unicode.

# UCS-4 (Universal Character Set)
# UCS-4 is a character encoding standard that uses 32 bits (4 bytes) to represent each character.

# UTF-8 (Unicode Transformation Format)
# UTF-8 is a variable-width character encoding capable of encoding all 1,112,064 valid code points in Unicode using one to four 8-bit bytes.
# UTF-8 is the most widely used Unicode encoding.
# UTF-8 uses as many bits for each of the code points as it really needs to represent them.

# UTF-16 (Unicode Transformation Format)
# UTF-16 is a variable-width character encoding capable of encoding all 1,112,064 valid code points in Unicode using one to four 16-bit words.
# UTF-16 uses as many bits for each of the code points as it really needs to represent them.

# BOM 
# BOM (Byte Order Mark) is a special combination of bits announcing encoding used by a file's content (eg. UCS-4 or UTF-B).
# BOM is a Unicode character (U+FEFF) that is used to mark the beginning of a text stream,
#   and to indicate that the text stream is encoded in Unicode.









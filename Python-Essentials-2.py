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


# STRINGS AS SEQUENCE
# Indexing

# Python strings are sequences.
# A sequence is a collection of objects that are stored in a particular order and can be accessed through an index.

# Iterating


#  NOTE
# Python strings are immutable,
#   which means that you cannot change the content of a string once it has been created.
#   the similarity of strings and lists is limited.
#       doesn't allow you to use the 'del' instruction to remove anything from a string
#       doesn't allow you to use the 'append' or 'extend' methods to add anything to a string, 
#           Python strings don't have the append() method – you cannot expand them in any way.
#       doesn't allow you to use the 'insert' method to insert anything into a string
#   You can only use the 'del' to remove the whole string


# STRING OPERATIONS

# min()
# The function finds the minimum element of the sequence passed as an argument.
#   The sequence can be a string, a list, or a tuple.
#   The sequence CANNOT be empty.

# max()
# The function finds the maximum element of the sequence passed as an argument.


# STRING METHODS

# capitalize()
# The method returns a copy of the string with its first character capitalized and the rest lowercased.

# casefold()
# The method returns a copy of the string with all the case-based characters (letters) lowercased.

# center()
# The method returns a copy of the string with the specified number of characters centered in it.
#   If the number of characters is less than the length of the string, the original string is returned.

# count()
# The method returns the number of occurrences of a substring in the string.

# endswith()
# The method returns True if the string ends with the specified suffix, False otherwise.

# find()
# The method returns the index of the first occurrence of the specified substring in the string.
#   If the substring is not found, the method returns -1.

#  LAB   
# Your own split

# Your task is to write your own function, which behaves almost exactly like the original split() method, i.e.:

#   it should accept exactly one argument – a string;
#   it should return a list of words created from the string, divided in the places where the string contains whitespaces;
#   if the string is empty, the function should return an empty list;
#   its name should be mysplit()

def mysplit(strng):

    list_of_words = []
    word = ""
    for i in range(len(strng)):
        if strng[i] != " ":
            word += strng[i]
        else:
            list_of_words.append(word)
            word = ""
    list_of_words.append(word)
    return list_of_words

print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))


# LAB
# A LED Display

# You've surely seen a seven-segment display.
# It's a device (sometimes electronic, sometimes mechanical) designed to present one decimal digit 
# using a subset of seven segments.

# EXAMPLE

  # ### ### # # ### ### ### ### ### ###
  #   #   # # # #   #     # # # # # # # 
  # ### ### ### ### ###   # ### ### # # 
  # #     #   #   # # #   # # #   # # # 
  # ### ###   # ### ###   # ### ### ###


# TASK
# Your code has to display any non-negative integer number entered by the user.
digits = [ '1111110',  	# 0
	   '0110000',	# 1
	   '1101101',	# 2
	   '1111001',	# 3
	   '0110011',	# 4
	   '1011011',	# 5
	   '1011111',	# 6
	   '1110000',	# 7
	   '1111111',	# 8
	   '1111011',	# 9
	   ]
7
def print_number(num):
	global digits
	digs = str(num)
	lines = [ '' for lin in range(5) ]
	for d in digs:
		segs = [ [' ',' ',' '] for lin in range(5) ]
		ptrn = digits[ord(d) - ord('0')]
		if ptrn[0] == '1':
			segs[0][0] = segs[0][1] = segs[0][2] = '#'
		if ptrn[1] == '1':
			segs[0][2] = segs[1][2] = segs[2][2] = '#'
		if ptrn[2] == '1':
			segs[2][2] = segs[3][2] = segs[4][2] = '#'
		if ptrn[3] == '1':
			segs[4][0] = segs[4][1] = segs[4][2] = '#'
		if ptrn[4] == '1':
			segs[2][0] = segs[3][0] = segs[4][0] = '#'
		if ptrn[5] == '1':
			segs[0][0] = segs[1][0] = segs[2][0] = '#'
		if ptrn[6] == '1':
			segs[2][0] = segs[2][1] = segs[2][2] = '#'
		for lin in range(5):
			lines[lin] += ''.join(segs[lin]) + ' '
	for lin in lines:
		print(lin)

print_number(int(input("Enter the number you wish to display: ")))

# SECTION SUMMARY
# 1. Strings are key tools in modern data processing, as most useful data are actually strings. 
# For example, using a web search engine (which seems quite trivial these days) utilizes extremely complex string processing, involving unimaginable amounts of data.

# 2. Comparing strings in a strict way (as Python does) can be very unsatisfactory when it comes to advanced searches 
# (e.g. during extensive database queries). 
# Responding to this demand, a number of fuzzy string comparison algorithms has been created and implemented. 
# These algorithms are able to find strings which aren't equal in the Python sense, but are similar.

# One such concept is the Hamming distance, which is used to determine the similarity of two strings. 
# If this problem interests you, you can find out more about it here: https://en.wikipedia.org/wiki/Hamming_distance. 
# Another solution of the same kind, but based on a different assumption, is the Levenshtein distance 


# 3. Another way of comparing strings is finding their acoustic similarity, 
# which means a process leading to determine if two strings sound similar (like "raise" and "race"). 
# Such a similarity has to be established for every language (or even dialect) separately.

# An algorithm used to perform such a comparison for the English language is called Soundex and was invented – you won't believe – in 1918. 
# You can find out more about it here: https://en.wikipedia.org/wiki/Soundex.

# 4. Due to limited native float and integer data precision, 
# it's sometimes reasonable to store and process huge numeric values as strings. 
# This is the technique Python uses when you force it to operate on an integer number consisting of a very large number of digits.



# ERRORS
# Murphy's law: Anything that can go wrong, will go wrong.
# 
import math

x = float(input("Enter x: "))
y = math.sqrt(x) # that the sqrt() function fails if it gets a negative argument. 

print("The square root of", x, "equals to", y)
# there is no guarantee that the string can be converted into a float value 
# (the user may enter a string which cannot be interpreted as a number, e.g., "abc")


# EXCEPTIONS
# An exception is an event which occurs during the execution of a program that disrupts the normal flow of the program's instructions.

# Python always raises an exception (or that an exception has been raised) when it has no idea what to do with your code.

# Handling an Exception
# Python implements a try keyword


first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))

try:
    print(first_number / second_number)
except:
    print("This operation cannot be done.")

print("THE END.")
    
# Note:

# the try keyword begins a block of the code which may or may not be performing correctly;
# next, Python tries to perform the risky action; if it fails, an exception is raised and Python starts to look for a solution;
# the except keyword starts a piece of code which will be executed if anything inside the try block goes wrong – if an exception is raised inside a previous try block, it will fail here, so the code located after the except keyword should provide an adequate reaction to the raised exception;
# returning to the previous nesting level ends the try-except section.
    
try:
    print("1")
    x = 1 / 0
    print("2") # the print("2") instruction was lost in the process.
except:
    print("Oh dear, something went wrong...")

print("3")

try:
    x = int(input("Enter a number: "))
    y = 1 / x
except:
    print("Oh dear, something went wrong...")

print("THE END.")

# Note:

# the try-except block is able to catch all exceptions, but it's not a good idea to use it blindly 
# 	– it may hide some bugs in your code;

# If a number is not entered, 
# The message: Oh dear, something went wrong... appearing in the console says nothing about the reason
# there are two possible causes of the exception:
#	non-integer data entered by the user;
#	 an integer value equal to 0 assigned to the x variable.

# SOLUTION
# build two consecutive try-except blocks, 
# 	one for each possible exception reason (easy, but will cause unfavorable code growth)
# use a more advanced variant of the instruction.


try:
	x = int(input("Enter a number: "))
	y = 1 / x
	print(y)
except ZeroDivisionError:
	print("You cannot divide by zero, sorry.")
except ValueError:
	print("You must enter an integer value.")
except:
	print("Oh dear, something went wrong...")
print("THE END.")

# NOTE:

# the except branches are searched in the same order in which they appear in the code;

# you must not use more than one except branch with a certain exception name;

# the number of different except branches is arbitrary 
# 	– the only condition is that if you use try, you must put at least one except (named or not) after it;

# the except keyword must not be used without a preceding try;

# if any of the except branches is executed, no other branches will be visited;

# if none of the specified except branches matches the raised exception, the exception remains unhandled

# if an unnamed except branch exists (one without an exception name), it has to be specified as the last.


try:
    # except ZeroDivisionError has been removed
    x = int(input("Enter a number: ")) # What happens now if the user enters 0 as an input?
    y = 1 / x 
    print(y)

except ValueError:
    print("You must enter an integer value.")
except:
    print("Oh dear, something went wrong...")

print("THE END.")
    

# What happens now if the user enters 0 as an input?

# As there are no dedicated branches for division by zero, 
# the raised exception falls into the general (unnamed) branch


# SECTION SUMMARY
# 1. An exception is an event during program execution caused by an abnormal situation. 
# The exception should he handled to avoid the termination of the program. 
# The part of your code that is suspected of being the source of the exception should be put inside the try branch.

# When the exception happens, the execution of the code is not terminated, 
# but instead jumps into the except branch. 
# This is the place where the handling of the exception should take place. 
# The general scheme for such a construction looks as follows:


try:
    # :
    # Risky code.
    # :
except:
    # :
    # Crisis management takes place here.
    # :
# :
# Back to normal.
# :
 
# 2. If you need to handle more than one exception coming from the same try branch, 
# you can add more than one except branch, but you have to label them with different exception names, like this:

# :
try:
    # :
    # Risky code.
    :
except Except_1:
    # Crisis management takes place here.
except Except_2:
    # We save the world here.
# :
# Back to normal.
# :
 
# At most, one of the except branches is executed 
# 	– none of the branches is performed when the raised exception doesn't match any of the specified exceptions.


# 3. You cannot add more than one anonymous (unnamed) except branch after the named ones.

# The code that always runs smoothly.
# :
	try:
    # :
    # Risky code.
    # :
except Except_1:
    # Crisis management takes place here.
except Except_2:
    # We save the world here.
	except:
    # All other issues fall here.
# :
# Back to normal.
# :


# 4. You can use the else keyword to mark a block of code to be executed if no exceptions were raised in the try block.
# :
	try:
	# :
	# Risky code.
	# :
	except Except_1:
	# Crisis management takes place here.	
	

# EXCEPTIONS
# Is an event which occurs during the execution of a program that disrupts the normal flow of the program's instructions.
# The program can be interrupted by an exception, and the program can be interrupted by a keyboard interrupt.


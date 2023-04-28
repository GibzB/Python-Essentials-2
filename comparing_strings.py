# Python strings can be compared using the same set of operators which are in use in relation to numbers.

# The result of the comparison is always Boolean: True or False.

# The operators are:

# == (equal to)
# != (not equal to)
# > (greater than)
# < (less than)
# >= (greater than or equal to)
# <= (less than or equal to)

# The comparison rules are simple:

# two strings are equal when they consist of the same symbols in the same order
# a string is considered to be smaller than another if it comes first in lexicographical order
# the comparison between strings is case-sensitive – the uppercase letters are considered to be smaller than the lowercase ones
# the comparison between strings is performed in the same way as the comparison between numbers, character by character
# the comparison ends when two characters differ (as in the example above) or when the shorter string is exhausted
# if two strings are equal, their lengths are irrelevant
# if you want to compare two strings in a case-insensitive way, you need to use the lower() or upper() method to normalize them first
# the comparison operators are overloaded – they can be used to compare not only strings but also other sequences like lists or tuples

# Let's look at some examples:

# Code	Result
"alpha" == "alpha"	#True
"alpha" != "Alpha"	#True
"alpha" < "alphabet"	#True
"alpha" > "alphabet"	#False
"alpha" < "alphabet"	#True
"alpha" <= "alphabet"	#True
"alpha" <= "alpha"	#True
"alpha" >= "alphabet"	#False
"alpha" >= "alpha"	#True
"alpha" >= "Alpha"	#True

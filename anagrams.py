# An anagram is a new word formed by rearranging the letters of a word, using all the original letters exactly once
# For example, the phrases "rail safety" and "fairy tales" are anagrams, while "I am" and "You are" are not.

# The program tasks:

# asks the user for two separate texts;
# checks whether, the entered texts are anagrams and prints the result.

# Note:
# assume that two empty strings are not anagrams;
# treat upper- and lower-case letters as equal;
# spaces are not taken into account during the check – treat them as non-existent

# Solution:
# Ask the user for two separate texts
text1 = input("Enter the first word: ")
text2 = input("Enter the second word: ")

# Remove all spaces
text1 = text1.replace(' ','')
text2 = text2.replace(' ','')

# Check if the words are anagrams
if len(text1) > 1 and len(text2) > 1 and text1.upper() == text2[::-1].upper():
    print("These words are anagrams")
else:
    print("These words are not anagrams")





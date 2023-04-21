multiline = '''Line #1
Line #2'''
# Line #1 contains seven characters. Two such lines comprise 14 characters
# The missing character is simply invisible – it's a whitespace. Just after #1. Usually denoted by (\n)
print(len(multiline))

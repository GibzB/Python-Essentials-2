# 

from platform import python_implementation, python_version_tuple

print(python_implementation())

for atr in python_version_tuple():
    print(atr)


# The output of the program is as follows:
#
# CPython
# 3
# 8
# 2

# The map is a built-in Python function
# used by programmers to make the
# progranm simpler. This function
# iterates up on all the specified
# elements without the usage of any
# loops.



def add_list(a,b):
    return a+b
output = list(map(add_list,[2,3,5],[6,8,10]))
print(output)
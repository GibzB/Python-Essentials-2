# The filter is a built-in Python function, which is useful when it is required to segregate any kind of data. It is used to
#   extract or filter the data based on the given condition.

def is_positive(a):
    return a > 0
output = list(filter(is_positive,[1,-2,3,4,5,-3]))
print(output)
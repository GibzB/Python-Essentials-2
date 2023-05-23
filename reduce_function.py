# Used when it is required to apply the same operation to all the elements in the given list.

import functools
def sum_two_elements(a,b):
    return a+b

numbers = [2,4,1,3,9]
result = functools.reduce(sum_two_elements,numbers)
print(result)
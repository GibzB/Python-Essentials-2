# # It is known as anonymous because we
# can instantiate and declare a function
# without a name.

# If you have a single operation to be
# executed, the lambda function is
# extremely useful instead of declaring
# a traditional function. Lambda is
# similar to the function, except it can
# only return only one expression.


answer = lambda a, b: a**2 + b**2 + 2*(a+b)
print(answer(3,6))
def bad_fun(n):
    return 1 / n

try:
    bad_fun(0)
except ArithmeticError:
    print("What happened? An exception was raised!")

print("THE END.")

# Note: the exception raised can cross function and module boundaries, 
#   and travel through the invocation chain looking for a matching except clause able to handle it.

# If there is no such clause, the exception remains unhandled, 
#   and Python solves the problem in its standard way – by terminating your code and emitting a diagnostic message.
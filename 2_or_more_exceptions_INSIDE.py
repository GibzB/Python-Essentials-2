# The ZeroDivisionError exception (being a concrete case of the ArithmeticError exception class) is raised INSIDE the bad_fun() function, 
#   and it doesn't leave the function – the function itself takes care of it.

def bad_fun(n):
    try:
        return 1 / n
    except ArithmeticError:
        print("Arithmetic Problem!")
    return None

bad_fun(0)

print("THE END.")


# implementing a simple module import
from module import suml, prodl

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(suml(zeroes))
print(prodl(ones))



# __pycache__ folder get created when main.py is run

# When a module is imported, its contents are implicitly executed by Python.
# The module is only imported once, even if it is imported multiple times.

# The __name__ variable is set to the name of the module when the module is imported.
# The __name__ variable is set to __main__ when the module is executed as a script.

# when you run a file directly, its __name__ variable is set to __main__;
# when a file is imported as a module, its __name__ variable is set to the file's name (excluding .py)
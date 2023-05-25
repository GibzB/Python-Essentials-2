# task is to extend the Stack class behavior in such a way so that the class is able to count all the elements that are pushed and popped (we assume that counting pops is enough). Use the Stack class we've provided in the editor.

# Follow the hints:

# introduce a property designed to count pop operations and name it in a way which guarantees it is hidden;
# initialize it to zero inside the constructor;
# provide a method which returns the value currently assigned to the counter (name it get_counter()).

class Stack:
    def __init__(self):
        self.__stk = []

    def push(self, val):
        self.__stk.append(val)

    def pop(self):
        val = self.__stk[-1]
        del self.__stk[-1]
        return val


class CountingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__counter = 0

        def get_counter(self):
            return self.__counter

            def pop(self):
                self.__counter += 1
                return Stack.pop(self)

                stk = CountingStack()
for i in range(100):
    stk.push(i)
    stk.pop()
print(stk.get_counter())
    
# OOP: Properties

# Instance Variables
# Instance variables are variables that are tied to an object. 
# Instance variables are tied to the object that the class is instantiated on.
# Instance variables are defined in the constructor.
# Instance variables are accessed using the self keyword.

# A class can be equipped with two different kinds of data to form a class's properties.
# This kind of class property exists when and only when it is explicitly created and added to an object. 

#  Important consequences:

# different objects of the same class may possess different sets of properties;
# there must be a way to safely check if a specific object owns the property you want to utilize (unless you want to provoke an exception – it's always worth considering)
# each object carries its own set of properties – they don't interfere with one another in any way.

class ExampleClass: # the class named ExampleClass has a constructor,
                    # which unconditionally creates an instance variable named first, and sets it with the value passed through the first argument (from the class user's perspective) or the second argument (from the constructor's perspective); 
                    # note the default value of the parameter
    def __init__(self, val = 1):
        self.first = val

    def set_second(self, val): # the class also has a method which creates another instance variable, named second
        self.second = val


example_object_1 = ExampleClass() # example_object_1 only has the property named first
example_object_2 = ExampleClass(2)
# example_object_2 has two properties: first and second
example_object_2.set_second(3) 

example_object_3 = ExampleClass(4)
example_object_3.third = 5 # example_object_3 has been enriched with a property named third just on the fly, outside the class's code

print(example_object_1.__dict__)
print(example_object_2.__dict__)
print(example_object_3.__dict__)

# NOTE
# modifying an instance variable of any object has no impact on all the remaining objects.

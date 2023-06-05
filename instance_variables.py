class ExampleClass:
    def __init__(self, val = 1):
        self.__first = val

    def set_second(self, val = 2):
        self.__second = val


example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)

example_object_2.set_second(3)

example_object_3 = ExampleClass(4)
example_object_3.__third = 5


print(example_object_1.__dict__)
print(example_object_2.__dict__)
print(example_object_3.__dict__)
    
# NOTE
# The __dict__ attribute is a dictionary containing all the names of the object's properties and their corresponding values.
# The __dict__ attribute is created automatically when the object is created, and updated when the object's properties are modified.
# The __dict__ attribute is accessed using the dot operator.
# Two underscores make the instance variable PRIVATE

# When Python sees that you want to add an instance variable to an object and you're going to do it inside any of the object's methods, it mangles the operation in the following way:

# it puts a class name before your name;
# it puts an additional underscore at the beginning.
# This is why the __first becomes _ExampleClass__first


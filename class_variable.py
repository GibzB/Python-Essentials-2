# Class Variable

# Is a a property which exists in just one copy and is stored outside any object

# It's shared by all the objects of the class
# Is a shared variable
# Is defined within the class construction
# Is not prefixed with underscores

class ExampleClass:
    counter = 0
    def __init__(self, val = 1):
        self.__first = val
        ExampleClass.counter += 1


example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)
example_object_3 = ExampleClass(4)

print(example_object_1.__dict__, example_object_1.counter)
print(example_object_2.__dict__, example_object_2.counter)
print(example_object_3.__dict__, example_object_3.counter)

# There is an assignment in the first list of the class definition – it sets the variable named counter to 0; 
# initializing the variable inside the class but outside any of its methods makes the variable a class variable;

# Accessing such a variable looks the same as accessing any instance attribute 
#   – you can see it in the constructor body; as you can see, the constructor increments the variable by one; 
#       in effect, the variable counts all the created objects.
# Accessing the class variable is done with the __class__ keyword
#   – it's a reference to the class object itself, and not to any of its objects;
#   – the variable is accessed using the dot operator, just like any other object's attribute;


# class variables aren't shown in an object's __dict__ (this is natural as class variables aren't parts of an object) but you can always try to look into the variable of the same name, but at the class level – we'll show you this very soon;
# A class variable always presents the same value in all class instances (objects)

class ExampleClass:
    __counter = 0
    def __init__(self, val = 1):
        self.__first = val
        ExampleClass.__counter += 1


example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)
example_object_3 = ExampleClass(4)

print(example_object_1.__dict__, example_object_1._ExampleClass__counter)
print(example_object_2.__dict__, example_object_2._ExampleClass__counter)
print(example_object_3.__dict__, example_object_3._ExampleClass__counter)



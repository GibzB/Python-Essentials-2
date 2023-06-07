# Python's attitude to object instantiation raises one important issue – in contrast to other programming languages, you may not expect that all objects of the same class have the same sets of properties.
#
# This is true – Python doesn't require you to define all the object's properties inside the class definition. You can add them later, when the object is already instantiated.
#
# This is a very powerful feature, but it has its own price – you can't be sure that any object has a property you expect it to have.
#

class ExampleClass:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1


example_object = ExampleClass(1)

print(example_object.a)
print(example_object.b)
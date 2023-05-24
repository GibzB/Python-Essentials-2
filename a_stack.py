# Invoke these functions to push and pop values. 
# This means that they should both be accessible to every class's user


class Stack:
    def __init__(self):
        self.__stack_list = []

    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val

# There are two stacks created from the same base class. 
# They work independently.
stack_object = Stack()

stack_object.push(3)
stack_object.push(2)
stack_object.push(1)

print(stack_object.pop())
print(stack_object.pop())
print(stack_object.pop())

# Having such a class opens up some new possibilities. 
# For example, you can now have more than one stack behaving in 
# the same way. Each stack will have its own copy of private data, 
# but will utilize the same set of methods.

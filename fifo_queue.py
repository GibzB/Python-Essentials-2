# Task is to implement the Queue class with two basic operations:

# put(element), which puts an element at end of the queue;
# get(), which takes an element from the front of the queue and returns it as the result (the queue cannot be empty to successfully perform it.)
# Follow the hints:

# use a list as your storage (just like we did with the stack)
# put() should append elements to the beginning of the list, while get() should remove the elements from the end of the list;
# define a new exception named QueueError (choose an exception to derive it from) and raise it when get() tries to operate on an empty list.

# Expected output:
# 1
# dog
# False
# Queue error

class QueueError(IndexError):  # Base class for the new exception.
    pass


class Queue:
    def __init__(self):
        self.__queue = []

    def put(self, elem):
        self.__queue.append(elem)

    def get(self):
        if len(self.__queue) == 0:
            raise QueueError
        elem = self.__queue[0]
        del self.__queue[0]
        return elem


que = Queue()
que.put(1)
que.put("dog")
que.put(False)
try:
    for i in range(4):
        print(que.get())
except:
    print("Queue error")
    
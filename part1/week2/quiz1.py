'''
1. Queue with two stacks. Implement a queue with two stacks so that each queue
operations takes a constant amortized number of stack operations.
'''
class Stack:
    class Node:
        def __init__():
            self.item = None
            self.next = None
    def __init__():
        self.head = None
    # I think they won't make me implment the stack again, can just explain api.



class Queue:
    def __init__():
        self.dequeue_stack = Stack()
        self.temp_stack = Stack()

    def enqueue(self, item):
        # First empty the enqueue stack onto temp_stack
        while !self.dequeue_stack.is_empty():
            self.temp_stack.push(self.dequeue_stack.pop())
        # Put the item onto the dequeue_stack
        self.dequeue_stack.push(item)
        # Re add in the elements that were in dequeue_stack
        while !self.temp_stack.is_empty():
            self.dequeue_stack.push(self.temp_stack.pop())

    def dequeue(self):
        self.dequeue_stack.pop()

    def is_empty(self):
        return self.dequeue_stack.is_empty()

    def size(self):
        return self.dequeue_stack.size()


'''
2. Stack with max. Create a data structure that efficiently supports the
stack operations (push and pop) and also a return-the-maximum operation.
Assume the elements are reals numbers so that you can compare them.
'''
class Stack:
    class Node:
        def __init__():
            self.item = None
            self.next = None

    def __init__():
        self.head = None
        self.values = []

    def push(self, item):
        self.values.append(item)

        old_head = self.head
        self.head = Node()
        self.head.item = item
        self.head.next = old_head

    def pop(self):
        item = self.head.item
        self.head = self.head.next

        self.values.remove(item)
        return item

    def max(self):
        sorted(self.values) # n log n
        return self.values[-1]

'''
THE ACTUAL ANSWER, hint: Use two stacks, one to store all of the items and a second stack to store the maximums.
see here for more help: http://stackoverflow.com/questions/685060/design-a-stack-such-that-getminimum-should-be-o1
'''
class StackWithMax():
    def __init__():
        self.stack = Stack()
        self.max_stack = Stack()
        self.max = None

    def pop():
        self.max = self.max_stack.pop()
        return self.stack.pop()

    def push(self, item):
        self.stack.push(item)
        if item > self.max:
            self.max_stack.push(item)
        else:
            self.max_stack.push(self.max)

    def max(self):
        return self.max

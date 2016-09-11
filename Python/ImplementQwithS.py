'''
can only use list(stack) function: append(), pop(), empty(), size(), peek()
'''

class Queue():
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.storage_stack = list()  # for push
        self.buffer_stack = list()  # for pop


    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.storage_stack.append(x)


    def pop(self):
        """
        :rtype: nothing
        """
        if len(self.buffer_stack) != 0:
            self.buffer_stack.pop()
        else:
            while len(self.storage_stack) != 0:
                self.buffer_stack.append(self.storage_stack.pop())
            self.buffer_stack.pop()


    def peek(self):
        """
        :rtype: int
        """
        if len(self.buffer_stack) != 0:
            return self.buffer_stack[-1]
        else:
            while len(self.storage_stack) != 0:
                self.buffer_stack.append(self.storage_stack.pop())
            return self.buffer_stack[-1]


    def empty(self):
        """
        :rtype: bool
        """
        if len(self.storage_stack) == 0 and len(self.buffer_stack) == 0:
            return True
        return False


q = Queue()
q.push(1)
q.push(2)
q.push(3)
print q.pop()
print q.pop()
q.push(4)
print q.peek()
print q.empty()
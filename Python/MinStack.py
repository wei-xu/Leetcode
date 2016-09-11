from Queue import PriorityQueue
class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = list()
        self.min_stack = list()

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.stack.append(x)
        if len(self.min_stack) == 0:
            self.min_stack.append(x)
        else:
            # self.min_stack.append(min(x, self.min_stack[-1]))
            if self.min_stack[-1] >= x:
                self.min_stack.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        out = self.stack.pop()
        if out == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]


    def getMin(self):
        """
        :rtype: int
        """
        return self.min_stack[-1]

s = MinStack()
s.push(2)
s.push(3)
s.push(1)
s.push(4)
print s.getMin()
s.pop()
print s.getMin()
s.pop()
print s.getMin()
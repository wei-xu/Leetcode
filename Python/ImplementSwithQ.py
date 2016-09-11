from collections import deque
class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.top_loc = 1  # 1 means top is at queue1, 2 at queue 2
        self.queue1 = deque()
        self.queue2 = deque()

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        if self.top_loc == 1:
            if len(self.queue1) == 0:
                self.queue1.append(x)
            else:
                self.queue2.append(self.queue1.popleft())
                self.queue1.append(x)
        else:
            if len(self.queue2) == 0:
                self.queue2.append(x)
            else:
                self.queue1.append(self.queue2.popleft())
                self.queue2.append(x)


    def pop(self):
        """
        :rtype: nothing
        """
        if self.top_loc == 1:
            tmp = self.queue1.popleft()
            while len(self.queue2) > 1:
                self.queue1.append(self.queue2.popleft())
            self.top_loc = 2
            return tmp
        else:
            tmp = self.queue2.popleft()
            while len(self.queue1) > 1:
                self.queue2.append(self.queue1.popleft())
            self.top_loc = 1
            return tmp


    def top(self):
        """
        :rtype: int
        """
        if self.top_loc == 1:
            return self.queue1[0]
        else:
            return self.queue2[0]

    def empty(self):
        """
        :rtype: bool
        """
        if len(self.queue1) == 0 and len(self.queue2) == 0:
            return True
        return False


s = Stack()
s.push(1)
print s.empty()
print s.top()
print s.pop()
print s.empty()
s.push(1)
s.push(2)
s.push(3)
print s.top()
print s.pop()
print s.top()
print s.pop()
print s.pop()
print s.empty()

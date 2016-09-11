class ZigzagIterator(object):
    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.num_v = len(locals()) - 1
        self.all = list()
        self.total = 0
        for key in locals().keys()[:-1]:
            self.all.append(locals()[key])
            self.total += len(locals()[key])

        self.x = -1
        self.y = 0

    def next(self):
        """
        :rtype: int
        """
        if self.x == self.num_v:
            self.x = 0
            self.y += 1
            # if len(self.all[self.x]) > self.y:
            #     return self.all[self.x][self.y]
        tmpx = self.x
        tmpy = self.y
        for i in range(self.x + 1, self.num_v):
            if len(self.all[i]) > self.y:
                self.x = i
                break
        if self.x == tmpx:
            for j in range(0, self.x + 1):
                if len(self.all[j]) > self.y + 1:
                    self.x = j
                    self.y += 1
                    break
            if self.x == tmpx and self.y == tmpy:
                self.y = -1
        output = self.all[self.x][self.y]
        self.total -= 1
        return output

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.total == 0 or self.y == -1:
            return False
        return True

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
v1 = [1, 2]
v2 = [5, 6, 7, 8, 9, 20]
z = ZigzagIterator(v1, v2)
v = []
while z.hasNext(): v.append(z.next())
print v

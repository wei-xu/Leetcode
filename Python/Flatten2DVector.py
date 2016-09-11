class Vector2D(object):

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.vec2d = []
        if vec2d:
            self.vec2d = reduce(lambda x, y: x + y, vec2d)
        self.pos = 0

    def next(self):
        """
        :rtype: int
        """
        output = self.vec2d[self.pos]
        self.pos += 1
        return output

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.pos < len(self.vec2d)


# Your Vector2D object will be instantiated and called as such:

nums = [
    []
]

i, v = Vector2D(nums), []
while i.hasNext(): v.append(i.next())
print v
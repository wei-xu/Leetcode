# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution(object):

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        l = root.left
        r = root.right
        return self.isSymmetricR(l, r)

    def isSymmetricR(self, l, r):
        if l is None and r is not None:
            return False
        if r is None and l is not None:
            return False
        if l is None and r is None:
            return True
        if l.val != r.val:
            return False
        if not self.isSymmetricR(l.left, r.right):
            return False
        if not self.isSymmetricR(l.right, r.left):
            return False
        return True

    def itSymmetric(self, root):
        if root is None:
            return True
        lq = deque()
        rq = deque()
        lq.append(root.left)
        rq.append(root.right)

        while len(lq) != 0:
            l = lq.popleft()
            r = rq.popleft()
            if l is None and r is not None:
                return False
            if r is None and l is not None:
                return False
            if l is None and r is None:
                continue
            if l.val != r.val:
                return False
            lq.append(l.left)
            lq.append(l.right)
            rq.append(r.right)
            rq.append(r.left)

        return True
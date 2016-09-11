# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.queue = []
        p = root
        while p is not None:
            self.queue.append(p)
            p = p.left

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.queue

    def next(self):
        """
        :rtype: int
        """
        ret = self.queue.pop()
        p = ret.right
        while p is not None:
            self.queue.append(p)
            p = p.left
        return ret.val
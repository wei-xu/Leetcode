# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.longest = 1
        if root:
            self.helper(root, root.val, 1)
        return self.longest

    def helper(self, root, last, n):
        if not root:
            if self.longest < n:
                self.longest = n
            return
        if root.val == last + 1:
            self.helper(root.left, root.val, n + 1)
            self.helper(root.right, root.val, n + 1)
        else:
            if self.longest < n:
                self.longest = n
            self.helper(root.left, root.val, 1)
            self.helper(root.right, root.val, 1)
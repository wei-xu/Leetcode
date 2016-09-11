# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.count = k
        self.value = 0
        self.dfs(root, k)
        return self.value

    def dfs(self, root):
         if root is None:
             return
         self.dfs(root.left)
         self.count -= 1
         if self.count == 0:
             self.value = root.val
             return
         self.dfs(root.right)

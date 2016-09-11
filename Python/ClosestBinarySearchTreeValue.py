# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from util import buildBinaryTree
from Node import TreeNode

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        kid = root.left if target < root.val else root.right
        if not kid:
            return root.val
        res = self.closestValue(kid, target)
        return res if abs(res - target) < abs(root.val - target) else root.val

s = Solution()
root = TreeNode(3)
nums = [3, 2, 4, 1]
root = buildBinaryTree(root, nums, 1)
print s.closestValue(root, 4.14)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from util import *

class Solution:
    # def lowest_common_ancestor(self, root, p, q):
    #     if p.val == root.val or q.val == root.val:
    #         return root
    #     if p.val < root.val and q.val > root.val:
    #         return root
    #     elif p.val < root.val and q.val < root.val:
    #         return self.lowest_common_ancestor(root.left, p, q)
    #     else:
    #         return self.lowest_common_ancestor(root.right, p, q)
    def lowestCommonAncestor(self, root, p, q):
        if root is None:
            return None
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        return root

s = Solution()
root1 = TreeNode(2)
root1.left = TreeNode(1)
# root1.right = TreeNode(3)
# lca = s.lowest_common_ancestor(root, TreeNode(2), TreeNode(4))
lca = s.lowestCommonAncestor(root1, TreeNode(2), TreeNode(1))
print root1.val
print lca.val

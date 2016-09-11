# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from Node import TreeNode
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        output = list()
        level = list()
        if root is None:
            return output
        if root.left is not None:
            level.append(root.left)
        if root.right is not None:
            level.append(root.right)
        output.append([root.val])
        while len(level) != 0:
            level_int = list()
            tmp = list()
            for node in level:
                level_int.append(node.val)
                if node.left is not None:
                    tmp.append(node.left)
                if node.right is not None:
                    tmp.append(node.right)
            output.append(level_int)
            level = tmp
        return output[::-1]

s = Solution()
root = TreeNode(1)
print s.levelOrderBottom(root)
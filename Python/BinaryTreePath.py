# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from util import buildBinaryTree, printBinaryTree
from Node import TreeNode
class Solution(object):
    def binaryTreePaths(self, root):
        self.output = []
        if root is None:
            return self.output
        self.dfs(root, str(root.val))
        return self.output

    def dfs(self, root, path):
        if root.left is None and root.right is None:
            self.output.append(path)
        if root.left:
            self.dfs(root.left, path + "->" + str(root.left.val))
        if root.right:
            self.dfs(root.right, path + "->" + str(root.right.val))


s = Solution()
nums = [1, 2, 3]
root = TreeNode(1)
t = buildBinaryTree(root, nums, 1)
printBinaryTree(t)
print s.binaryTreePaths(t)
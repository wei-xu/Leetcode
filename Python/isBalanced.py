from util import buildBinaryTree
from util import printBinaryTree

# def isBalanced(root):
#     if root is None:
#         return True
#     if getMaxDepth(root) - getMinDepth(root) < 2:
#         return True
#     return False
#
def getMaxDepth(root):
    if root is None:
        return 0
    else:
        return 1 + max(getMaxDepth(root.left), getMaxDepth(root.right))

# def getMinDepth(root):
#     if root is None:
#         return 0
#     else:
#         return 1 + min(getMinDepth(root.left), getMinDepth(root.right))

def isBalanced(root):
    if root is None:
        return True
    else:
        if abs(getMaxDepth(root.left) - getMaxDepth(root.right)) < 2:
            return isBalanced(root.left) and isBalanced(root.right)
        return False


# nums = [1,2,2,3,3,3,3,4,4,4,4,4,4,None, None,5,5]
nums = [1, 2, 2, 3, None, ]
root = None
root = buildBinaryTree(root, nums, 1)
printBinaryTree(root)
print
print isBalanced(root)

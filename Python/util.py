from Node import TreeNode
from Node import ListNode

def buildBinaryTree(root, nums, i):
    if i > len(nums):
        return root
    num = nums[i - 1]
    root = TreeNode(num)
    if 2 * i <= len(nums) and not nums[2 * i - 1] is None:
        root.left = buildBinaryTree(root.left, nums, 2 * i)
    if 2 * i + 1 <= len(nums) and not nums[2 * i] is None:
        root.right = buildBinaryTree(root.right, nums, 2 * i + 1)
    return root

def printBinaryTree(root):
    if root is None:
        return
    printBinaryTree(root.left)
    print root.val, " ",
    printBinaryTree(root.right)

def printLinkedList(head):
    p = head
    while p != None:
        print "%d " % p.val,
        p = p.next
    print

def buildLinkedList(nums):
    if len(nums) == 0:
        return None
    head = ListNode(nums[0])
    p = head
    for i in range(1, len(nums)):
        new_node = ListNode(nums[i])
        p.next = new_node
        p = p.next
    return head


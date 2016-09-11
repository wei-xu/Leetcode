# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from util import buildLinkedList, printLinkedList
from Node import ListNode
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head is None:
            return None
        p1 = head
        p2 = head
        if n == 1:
            if head.next is None:
                return None
            p2 = p2.next
            while p2.next is not None:
                p2 = p2.next
                p1 = p1.next
            del p2
            p1.next = None
        else:
            for _ in range(n - 1):
                p2 = p2.next
            while p2.next is not None:
                p2 = p2.next
                p1 = p1.next
            # p1 is pointing at the node to be deleted
            # while p2 is pointing to the end
            q = p1.next
            p1.val = q.val
            p1.next = q.next
            del q
        return head

s = Solution()
nums = [1, 2, 3, 4, 5]
nums2 = [2]
nums3 = []
ls = buildLinkedList(nums)
ls2 = buildLinkedList(nums2)
ls3 = buildLinkedList(nums3)
new_list = s.removeNthFromEnd(ls3, 1)
printLinkedList(new_list)

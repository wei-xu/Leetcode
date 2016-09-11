'''
Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from util import printLinkedList
from util import buildLinkedList

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        last = head
        p = head.next
        while p is not None:
            if p.val == last.val:
                last.next = p.next
                q = p
                p = p.next
                del q
            else:
                last = p
                p = p.next
        return head

nums = [1,1,2]
nums2 = [1,1,2,3,3,2,3, 3]
l1 = buildLinkedList(nums2)
printLinkedList(l1)
# l2 = buildLinkedList(nums2)
# printLinkedList(l2)
s = Solution()
l1 = s.deleteDuplicates(l1)
printLinkedList(l1)

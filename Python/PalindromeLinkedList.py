# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from Node import ListNode
from util import buildLinkedList
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
            return True
        p1 = head
        p2 = head
        while p2.next is not None and p2.next.next is not None:
            p2 = p2.next.next
            p1 = p1.next
        # p1 is pointing at the mid
        # reverse the second part
        # p3 is the head of second part
        p3 = p1.next
        last_node = p3
        p4 = p3.next
        while p4 is not None:
            tmp = p4.next
            p4.next = last_node
            last_node = p4
            p4 = tmp

        p3.next = None
        # last_node is the head of the reversed second part
        t1 = last_node
        t2 = head
        while t1 is not None:
            if not t1.val == t2.val:
                return False
            t1 = t1.next
            t2 = t2.next
        return True


        

nums = []
s = Solution()
num = buildLinkedList(nums)
print s.isPalindrome(num)
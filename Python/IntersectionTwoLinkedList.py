# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        len_a = 0
        len_b = 0
        p1 = headA
        p2 = headB
        while p1 is not None:
            len_a += 1
            p1 = p1.next
        while p2 is not None:
            len_b += 1
            p2 = p2.next
        p1 = headA
        p2 = headB
        if len_a > len_b:
            for a in range(len_a - len_b):
                p1 = p1.next
        else:
            for b in range(len_b - len_a):
                p2 = p2.next
        while p1 != p2:
            p1 = p1.next
            p2 = p2.next
        return p1
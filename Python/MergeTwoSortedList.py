'''
Merge two sorted linked lists and return it as a new list.
The new list should be made by splicing together the nodes
of the first two lists.
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from util import printLinkedList
from util import buildLinkedList

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p1 = l1
        p2 = l2
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        else:
            if p1.val > p2.val:
                l3 = p2
                p2 = p2.next
            else:
                l3 = p1
                p1 = p1.next
        p3 = l3
        while p1 != None or p2 != None:
            if p1 is None:
                p3.next = p2
                break
            elif p2 is None:
                p3.next = p1
                break
            else:
                if p1.val > p2.val:
                    p3.next = p2
                    p2 = p2.next
                else:
                    p3.next = p1
                    p1 = p1.next
                p3 = p3.next
        return l3

l1 = [2]
l2 = [2]

lst1 = buildLinkedList(l1)
print "lst1: ",
printLinkedList(lst1)
lst2 = buildLinkedList(l2)
print "lst2: ",
printLinkedList(lst2)
s = Solution()
lst3 = s.mergeTwoLists(lst1, lst2)
print "lst3: ",
printLinkedList(lst3)
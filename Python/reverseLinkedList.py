from util import buildLinkedList
from util import printLinkedList

def reverseList(head):
    if head is None:
        return None
    p = head
    lastNode = p
    p = p.next
    head.next = None
    while p != None:
        nextNode = p.next
        p.next = lastNode
        lastNode = p
        p = nextNode
    return lastNode


nums = [1,1,2]
head = None
head = buildLinkedList(nums)
printLinkedList(head)
print
reverse_list = reverseList(head)
printLinkedList(reverse_list)
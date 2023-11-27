from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        values = []
        while head:
            values.append(head.val)
            head = head.next
        values.reverse()
        head = ListNode(values[0])
        node = head
        for i in range(1, len(values)):
            node.next = ListNode(values[i])
            node = node.next
        return head


    def printList(self, head: ListNode):
        while head:
            print(head.val, end=" ")
            head = head.next
        print()

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

Solution().printList(head)
Solution().printList(Solution().reverseList(head))
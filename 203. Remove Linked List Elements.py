from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return str(f"val: {self.val}, next: {self.next.val}")

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if not head:
            return None
        if head.val == val:
            head = head.next
            return self.removeElements(head, val)
        prev = head
        if head.next:
            curr = head.next
            while curr:
                if curr.val == val:
                    prev.next = curr.next
                else:
                    prev = curr
                curr = curr.next

        return head


    def printList(self, head: ListNode):
        while head:
            print(head.val, end=" ")
            head = head.next


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(6)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(4)
head.next.next.next.next.next = ListNode(5)
head.next.next.next.next.next.next = ListNode(6)

# head = ListNode(7)
# head.next = ListNode(7)
# head.next.next = ListNode(7)
# head.next.next.next = ListNode(1)

Solution().printList(head)
print()
Solution().printList(Solution().removeElements(head, 6))


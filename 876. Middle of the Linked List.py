from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        self.length = self.get_length(head)
        middle = self.length // 2 + 1
        i = 1
        while i != middle:
            head = head.next
            i += 1
        return head

    def get_length(self, head: Optional[ListNode], length: int = 0) -> int:
        if not head:
            return length
        return self.get_length(head.next, length + 1)
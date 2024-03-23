from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return str(self.val)

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        self.values = []

        def helper(node: Optional[ListNode]):
            if node:
                self.values.append(node.val)
                helper(node.next)

        helper(head)

        self.values_reorder = []
        i = 0
        j = len(self.values) - 1
        while i <= j:
            self.values_reorder.append(self.values[i])
            self.values_reorder.append(self.values[j])
            i += 1
            j -= 1
        self.values_reorder = self.values_reorder[1:]

        def reorder(node: Optional[ListNode], index: int = 0):
            if node.next:
                node.next.val = self.values_reorder[index]
                reorder(node.next, index + 1)

        reorder(head)


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

print(Solution().reorderList(head))

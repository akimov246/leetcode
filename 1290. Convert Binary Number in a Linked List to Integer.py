# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        n = ''

        def helper(node: ListNode):
            if node:
                nonlocal n
                n += str(node.val)
                helper(node.next)

        helper(head)
        return int(n, 2)


head = ListNode(1)
head.next = ListNode(0)
head.next.next = ListNode(1)

print(Solution().getDecimalValue(head))
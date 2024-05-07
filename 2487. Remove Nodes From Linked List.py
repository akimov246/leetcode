#from sys import setrecursionlimit
from typing import Optional

#setrecursionlimit(10000)

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return str(self.val)

# Решение рабочее, но не проходит по memory limit
# class Solution:
#     def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
#
#         self.head = head
#
#         def helper(node: Optional[ListNode], prev: Optional[ListNode] = None):
#             if node.next is None:
#                 return self.head
#             if node.val < node.next.val:
#                 if prev is None:
#                     self.head = node.next
#                 else:
#                     prev.next = node.next
#                     node.next = None
#                 return helper(self.head)
#             return helper(node.next, node)
#
#         return helper(self.head)

class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ll_values = []
        while head:
            ll_values.append(head.val)
            head = head.next
        ll_values.reverse()
        mll_values = []
        prev = 0
        for val in ll_values:
            if val >= prev:
                prev = val
                mll_values.append(val)
        self.head = ListNode(mll_values.pop())
        head = self.head
        while mll_values:
            head.next = ListNode(mll_values.pop())
            head = head.next
        return self.head



head = ListNode(5)
head.next = ListNode(2)
head.next.next = ListNode(13)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(8)

result = Solution().removeNodes(head)

def inspect(node):
    values = []
    while node:
        values.append(node.val)
        node = node.next
    return values

print(inspect(result))
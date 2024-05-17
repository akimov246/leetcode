from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        def helper(node: Optional[ListNode], buffer: str = ''):
            if node:
                buffer += str(node.val)
                return helper(node.next, buffer)
            return buffer

        int_l1 = int(helper(l1)[::-1])
        int_l2 = int(helper(l2)[::-1])
        result_list = [int(n) for n in str(int_l1 + int_l2)]
        node = ListNode(result_list.pop())
        head = node
        while result_list:
            node.next = ListNode(result_list.pop())
            node = node.next
        return head


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

print(Solution().addTwoNumbers(l1, l2))



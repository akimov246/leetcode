from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'{self.val}'

class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        self.new_head = None

        def helper(node: Optional[ListNode], first_null: bool = True):
            if node.next:
                if node.val == 0:
                    if first_null:
                        if self.new_head is None:
                            self.new_node = ListNode(0)
                            self.new_head = self.new_node
                        first_null = False
                        helper(node.next, first_null)
                    else:
                        self.new_node.next = ListNode(0)
                        self.new_node = self.new_node.next
                        first_null = True
                        helper(node, first_null)
                else:
                    self.new_node.val += node.val
                    helper(node.next, first_null)

        helper(head)
        return self.new_head

head = ListNode(0)
head.next = ListNode(3)
head.next.next = ListNode(1)
head.next.next.next = ListNode(0)
head.next.next.next.next = ListNode(4)
head.next.next.next.next.next = ListNode(5)
head.next.next.next.next.next.next = ListNode(2)
head.next.next.next.next.next.next.next = ListNode(0)

print(Solution().mergeNodes(head))
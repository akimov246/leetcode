from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return None
        node = list1
        list = []
        while node:
            list.append(node.val)
            node = node.next
        node = list2
        while node:
            list.append(node.val)
            node = node.next
        list.sort()

        tmp = ListNode(list[0])
        result = tmp
        for i in range(1, len(list)):
            tmp.next = ListNode(list[i])
            tmp = tmp.next

        return result






list1 = ListNode(1)
list1.next = ListNode(2)
list1.next.next = ListNode(4)

list2 = ListNode(1)
list2.next = ListNode(3)
list2.next.next = ListNode(4)

result = Solution().mergeTwoLists(list1, list2)
node = result
while node:
    print(node.val)
    node = node.next
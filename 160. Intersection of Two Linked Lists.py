from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        passedA = set()
        passedB = set()
        while headA or headB:
            if headA not in passedA:
                passedA.add(headA)
            if headB not in passedB:
                passedB.add(headB)
            intersection = passedA.intersection(passedB)
            if intersection:
                return intersection.pop()
            if headA and headA.next:
                headA = headA.next
            else:
                headA = None
            if headB and headB.next:
                headB = headB.next
            else:
                headB = None
        return None

# listA = ListNode(4)
# listA.next = ListNode(1)
# listA.next.next = ListNode(8)
# listA.next.next.next = ListNode(4)
# listA.next.next.next.next = ListNode(5)
# listB = ListNode(5)
# listB.next = ListNode(6)
# listB.next.next = ListNode(1)
# listB.next.next.next = listA.next.next
listA = ListNode(2)
listA.next = ListNode(6)
listA.next.next = ListNode(4)
listB = ListNode(1)
listB.next = ListNode(5)

print(Solution().getIntersectionNode(listA, listB))

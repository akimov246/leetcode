from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f'{self.val}'

class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> list[int]:
        critical_points = []

        prev = head
        current = head.next
        index = 2

        while current.next:
            if prev.val > current.val < current.next.val or prev.val < current.val > current.next.val:
                critical_points.append(index)
            prev = current
            current = current.next
            index += 1

        #print(critical_points)

        if len(critical_points) < 2:
            return [-1, -1]

        minDistance = float('inf')
        maxDistance = critical_points[-1] - critical_points[0]
        for i in range(1, len(critical_points)):
            minDistance = min(minDistance, critical_points[i] - critical_points[i - 1])

        return [minDistance, maxDistance]

head = ListNode(5)
head.next = ListNode(3)
head.next.next = ListNode(1)
head.next.next.next = ListNode(2)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(1)
head.next.next.next.next.next.next = ListNode(2)

print(Solution().nodesBetweenCriticalPoints(head))
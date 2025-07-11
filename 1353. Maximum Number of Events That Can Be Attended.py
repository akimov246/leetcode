#TimeLimit

class Solution:
    def maxEvents(self, events: list[list[int]]) -> int:
        events.sort(key=lambda item: (item[1], item[0]))


        attend = 0
        days = set()

        for event in events:
            start = event[0]
            end = event[1] + 1
            for d in range(start, end):
                if d not in days:
                    attend += 1
                    days.add(d)
                    break

        return attend


print(Solution().maxEvents([[1,5],[1,5],[1,5],[2,3],[2,3]]))
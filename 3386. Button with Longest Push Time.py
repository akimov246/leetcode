class Solution:
    def buttonWithLongestTime(self, events: list[list[int]]) -> int:
        result = None
        prev_time = 0
        maximum = 0
        for index, time in events:
            press = time - prev_time
            if press > maximum:
                maximum = press
                result = index
            elif press == maximum:
                result = min(result, index)
            prev_time = time

        return result


print(Solution().buttonWithLongestTime(events = [[9,4],[19,5],[2,8],[3,11],[2,15]]))
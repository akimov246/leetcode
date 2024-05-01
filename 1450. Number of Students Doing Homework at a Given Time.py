class Solution:
    def busyStudent(self, startTime: list[int], endTime: list[int], queryTime: int) -> int:
        result = 0
        for s, e in zip(startTime, endTime):
            if queryTime in range(s, e + 1):
                result += 1
        return result

print(Solution().busyStudent(startTime = [1,2,3], endTime = [3,2,7], queryTime = 4))
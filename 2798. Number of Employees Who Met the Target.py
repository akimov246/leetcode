class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: list[int], target: int) -> int:
        counter = 0
        for h in hours:
            if h >= target:
                counter += 1
        return counter

print(Solution().numberOfEmployeesWhoMetTarget(hours = [0,1,2,3,4], target = 2))
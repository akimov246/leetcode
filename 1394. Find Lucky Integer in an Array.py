class Solution:
    def findLucky(self, arr: list[int]) -> int:
        lucky = -1
        for a in set(arr):
            freq = arr.count(a)
            if a == freq:
                lucky = max(lucky, a)
        return lucky

print(Solution().findLucky(arr = [2,2,3,4]))
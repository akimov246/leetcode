class Solution:
    def numberOfPoints(self, nums: list[list[int]]) -> int:
        points = set()
        for n in nums:
            points.update(tuple(range(n[0], n[1] + 1)))
        return len(points)

print(Solution().numberOfPoints(nums = [[3,6],[1,5],[4,7]]))
class Solution:
    def distinctAverages(self, nums: list[int]) -> int:
        averages = set()
        while nums:
            a = min(nums)
            b = max(nums)
            nums.remove(a)
            nums.remove(b)
            averages.add((a + b) / 2)
        return len(averages)

print(Solution().distinctAverages(nums = [4,1,4,0,3,5]))
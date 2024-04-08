class Solution:
    def findNumbers(self, nums: list[int]) -> int:
        ans = 0
        for n in nums:
            if len(str(n)) % 2 == 0:
                ans += 1
        return ans

print(Solution().findNumbers(nums = [12,345,2,6,7896]))
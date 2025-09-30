class Solution:
    def minBitwiseArray(self, nums: list[int]) -> list[int]:
        ans = []
        for n in nums:
            for m in range(n):
                if m | (m + 1) == n:
                    ans.append(m)
                    break
            else:
                ans.append(-1)

        return ans


print(Solution().minBitwiseArray(nums = [222]))
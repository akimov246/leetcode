class Solution:
    def decompressRLElist(self, nums: list[int]) -> list[int]:
        ans = []
        for i in range(0, len(nums), 2):
            freq = nums[i]
            value = nums[i + 1]
            ans.extend([value] * freq)
        return ans

print(Solution().decompressRLElist(nums = [1,2,3,4]))
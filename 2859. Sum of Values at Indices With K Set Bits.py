class Solution:
    def sumIndicesWithKSetBits(self, nums: list[int], k: int) -> int:
        result = 0
        for i in range(len(nums)):
            if bin(i).count('1') == k:
                result += nums[i]

        return result

print(Solution().sumIndicesWithKSetBits(nums = [5,10,1,5,2], k = 1))
class Solution:
    def repeatedNTimes(self, nums: list[int]) -> int:
        n = len(nums) // 2
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
            if freq[num] == n:
                return num


print(Solution().repeatedNTimes(nums = [1,2,3,3]))
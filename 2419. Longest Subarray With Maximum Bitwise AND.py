class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        bitwise_and = max(nums)

        length = 1
        start_idx = 0

        while True:
            try:
                idx = nums.index(bitwise_and, start_idx)
            except:
                return length
            current_length = 0
            for i in range(idx, len(nums)):
                if nums[i] == bitwise_and:
                    current_length += 1
                else:
                    start_idx = i
                    break
            else:
                start_idx = i + 1
            length = max(length, current_length)

print(Solution().longestSubarray(nums = [1, 2, 3, 4]))
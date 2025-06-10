class Solution:
    def longestMonotonicSubarray(self, nums: list[int]) -> int:
        inc = 1
        dec = 1

        i = 1
        current = 1
        while i < len(nums):
            if nums[i] > nums[i - 1]:
                current += 1
            else:
                inc = max(inc, current)
                current = 1
            i += 1
        inc = max(inc, current)

        i = 1
        current = 1
        while i < len(nums):
            if nums[i] < nums[i - 1]:
                current += 1
            else:
                dec = max(dec, current)
                current = 1
            i += 1
        dec = max(dec, current)

        return max(inc, dec)

print(Solution().longestMonotonicSubarray(nums = [4, 3, 3]))
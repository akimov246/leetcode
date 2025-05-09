class Solution:
    def incremovableSubarrayCount(self, nums: list[int]) -> int:
        result = 1
        gap = 1

        while gap < len(nums):
            l = 0
            while l + gap < len(nums) + 1:
                prev = -float('inf')
                for i in range(len(nums)):
                    if i not in range(l, l + gap):
                        current = nums[i]
                        if current > prev:
                            prev = current
                        else:
                            break
                else:
                    result += 1
                l += 1
            gap += 1
        return result

print(Solution().incremovableSubarrayCount(nums = [8,7,6,6]))
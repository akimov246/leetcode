class Solution:
    def minimumSumSubarray(self, nums: list[int], l: int, r: int) -> int:
        min_sum = float('inf')

        for i in range(l, r + 1):
            j = i
            current_sum = sum(nums[:j])
            while j < len(nums):
                if current_sum > 0:
                    min_sum = min(min_sum, current_sum)
                current_sum -= nums[j - i]
                current_sum += nums[j]
                j += 1
            if current_sum > 0:
                min_sum = min(min_sum, current_sum)

        return min_sum if min_sum != float('inf') else -1


print(Solution().minimumSumSubarray(nums = [-2, 2, -3, 1], l = 2, r = 3))
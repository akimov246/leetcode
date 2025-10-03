class Solution:
    def hasIncreasingSubarrays(self, nums: list[int], k: int) -> bool:
        if k == 1:
            return True
        for i in range(len(nums) + 1 - 2 * k):
            for a, b in zip(range(i + 1, i + k), range(i + k + 1, i + 2 * k)):
                if (nums[a] <= nums[a - 1]) or (nums[b] <= nums[b - 1]):
                    break
            else:
                return True

        return False


print(Solution().hasIncreasingSubarrays(nums = [5,8,-2,-1], k = 2))
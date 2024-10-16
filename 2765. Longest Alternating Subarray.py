class Solution:
    def alternatingSubarray(self, nums: list[int]) -> int:
        result = -1

        i = 0

        while i < len(nums) - 1:
            j = i + 1
            m = 1
            while j < len(nums):
                if nums[j] - nums[j - 1] == m:
                    result = max(result, j - i + 1)
                    j += 1
                    m *= -1
                else:
                    break
            else:
                break
            i += 1

        return result


print(Solution().alternatingSubarray(nums = [2,3,4,3,4]))
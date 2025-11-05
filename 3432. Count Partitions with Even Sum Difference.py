class Solution:
    def countPartitions(self, nums: list[int]) -> int:
        result = 0
        for i in range(1, len(nums)):
            if (sum(nums[:i]) - sum(nums[i:])) % 2 == 0:
                result += 1

        return result


print(Solution().countPartitions(nums = [10,10,3,7,6]))
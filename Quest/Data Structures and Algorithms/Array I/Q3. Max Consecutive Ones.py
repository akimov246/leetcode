class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        result = 0
        counter = 0
        for i in range(len(nums)):
            if nums[i]:
                counter += 1
                result = max(result, counter)
            else:
                counter = 0

        return result


print(Solution().findMaxConsecutiveOnes(nums = [1,1,0,1,1,1]))
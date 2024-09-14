class Solution:
    def findTheArrayConcVal(self, nums: list[int]) -> int:
        result = 0
        while nums:
            if len(nums) > 1:
                result += int(str(nums.pop(0)) + str(nums.pop()))
            else:
                result += nums.pop()
        return result

print(Solution().findTheArrayConcVal(nums = [7,52,2,4]))
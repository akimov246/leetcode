class Solution:
    def countHillValley(self, nums: list[int]) -> int:
        temp_nums = nums
        nums = []
        for i in range(len(temp_nums)):
            if i == len(temp_nums) - 1 or temp_nums[i] != temp_nums[i + 1]:
                nums.append(temp_nums[i])
        result = 0
        if len(nums) < 3:
            return 0
        for i in range(1, len(nums) - 1):
            if nums[i - 1] < nums[i] > nums[i + 1] or nums[i - 1] > nums[i] < nums[i + 1]:
                result += 1
        return result

print(Solution().countHillValley(nums = [5,7,7,1,7]))
class Solution:
    def minMaxGame(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums.pop()
        new_nums = []
        for i in range(len(nums) // 2):
            if i % 2:
                new_nums.append(max(nums[2 * i], nums[2 * i + 1]))
            else:
                new_nums.append(min(nums[2 * i], nums[2 * i + 1]))
        return self.minMaxGame(new_nums)

print(Solution().minMaxGame(nums = [1,3,5,2,4,8,2,2]))
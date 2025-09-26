class Solution:
    def minOperations(self, nums: list[int]) -> int:
        operations = 0

        last_idx = 0
        while True:
            for i in range(last_idx, len(nums) - 2):
                if nums[i] == 0:
                    operations += 1
                    for j in range(3):
                        nums[i + j] = int(not nums[i + j])
                    last_idx = i + 1
                    break
            else:
                return -1 if 0 in nums else operations

print(Solution().minOperations(nums = [0,1,1,1,0,0]))
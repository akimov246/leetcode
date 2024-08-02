class Solution:
    def minSwaps(self, nums: list[int]) -> int:
        if len(set(nums)) == 1:
            return 0

        total = nums.count(1)
        nums += nums[:total]
        current = nums[:total]
        index = total
        zeros = current.count(0)
        diff = zeros
        while index != len(nums):
            if current.pop(0) == 0:
                zeros -= 1
            current.append(nums[index])
            if current[-1] == 0:
                zeros += 1
            diff = min(diff, zeros)
            index += 1

        return diff


print(Solution().minSwaps(nums = [0,1,0,1,1,0,0]))
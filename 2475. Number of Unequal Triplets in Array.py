class Solution:
    def unequalTriplets(self, nums: list[int]) -> int:
        result = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if len(set((nums[i], nums[j], nums[k]))) == 3:
                        result += 1
        return result

print(Solution().unequalTriplets(nums = [4,4,2,4,3]))
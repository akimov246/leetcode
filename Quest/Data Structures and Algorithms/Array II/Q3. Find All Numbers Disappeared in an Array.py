class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        return list(set(range(1, len(nums) + 1)) - set(nums))


print(Solution().findDisappearedNumbers(nums = [4,3,2,7,8,2,3,1]))
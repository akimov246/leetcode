class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        ans = set()
        set_nums = set(nums)
        for i in range(1, len(nums) + 1):
            if i not in set_nums:
                ans.add(i)
        return list(ans)

# Решение с Leetcode
class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        return list(set(range(1, len(nums) + 1)).difference(set(nums)))

print(Solution().findDisappearedNumbers([4,3,2,7,8,2,3,1]))
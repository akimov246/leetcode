class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        ans = []
        for x, y in zip(nums[: len(nums) // 2], nums[len(nums) // 2:]):
            ans.extend([x, y])

        return ans


print(Solution().shuffle(nums = [2,5,1,3,4,7], n = 3))
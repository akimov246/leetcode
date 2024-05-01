class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        result = []
        left = nums[:n]
        right = nums[n:]
        for x, y in zip(left, right):
            result.append(x)
            result.append(y)
        return result

print(Solution().shuffle(nums = [2,5,1,3,4,7], n = 3))
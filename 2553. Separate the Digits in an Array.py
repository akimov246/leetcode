class Solution:
    def separateDigits(self, nums: list[int]) -> list[int]:
        return [int(n) for n in ''.join(str(n) for n in nums)]

print(Solution().separateDigits(nums = [13,25,83,77]))
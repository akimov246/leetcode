class Solution:
    def hasTrailingZeros(self, nums: list[int]) -> bool:
        even = False
        for n in nums:
            if n % 2 == 0:
                if even:
                    return True
                even = True
        return False

print(Solution().hasTrailingZeros(nums = [1,3,5,7,9]))
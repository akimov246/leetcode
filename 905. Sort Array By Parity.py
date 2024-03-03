class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        even = []
        odd = []
        for n in nums:
            if n % 2:
                odd.append(n)
            else:
                even.append(n)
        return even + odd

print(Solution().sortArrayByParity(nums = [3,1,2,4]))
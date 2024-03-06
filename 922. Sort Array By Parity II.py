class Solution:
    def sortArrayByParityII(self, nums: list[int]) -> list[int]:
        odd = []
        even = []
        for n in nums:
            if n % 2:
                odd.append(n)
            else:
                even.append(n)
        return [odd.pop() if i % 2 else even.pop() for i in range(len(nums))]

print(Solution().sortArrayByParityII(nums = [4,2,5,7]))
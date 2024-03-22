class Solution:
    def prefixesDivBy5(self, nums: list[int]) -> list[bool]:
        ans = []
        nums = "".join(str(n) for n in nums)
        for i in range(len(nums)):
            ans.append(int(nums[:i + 1], 2) % 5 == 0)
        return ans


print(Solution().prefixesDivBy5(nums = [0,1,1]))

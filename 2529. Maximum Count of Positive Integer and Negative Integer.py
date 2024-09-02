class Solution:
    def maximumCount(self, nums: list[int]) -> int:
        neg = 0
        pos = 0
        for n in nums:
            if n < 0:
                neg += 1
            elif n > 0:
                pos += 1
        return max(neg, pos)




print(Solution().maximumCount(nums = [-3,-2,-1,0,0,1,2]))
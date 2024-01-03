class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        ans = 0
        consecutive = 0
        for num in nums:
            if num == 1:
                consecutive += 1
                if consecutive > ans:
                    ans = consecutive
            else:
                consecutive = 0
        return ans

print(Solution().findMaxConsecutiveOnes([1,1,0,1,1,1]))
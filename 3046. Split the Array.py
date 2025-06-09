class Solution:
    def isPossibleToSplit(self, nums: list[int]) -> bool:
        counter = {}
        for n in nums:
            counter[n] = counter.get(n, 0) + 1
            if counter[n] > 2:
                return False
        return True

print(Solution().isPossibleToSplit(nums = [1,1,2,2,3,4]))
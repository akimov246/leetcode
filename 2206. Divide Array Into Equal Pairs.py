class Solution:
    def divideArray(self, nums: list[int]) -> bool:
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        for num in set(nums):
            if counter[num] % 2:
                return False
        return True

print(Solution().divideArray(nums = [3,2,3,2,2,2]))
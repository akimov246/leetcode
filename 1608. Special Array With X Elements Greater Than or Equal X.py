class Solution:
    def specialArray(self, nums: list[int]) -> int:
        for x in range(len(nums) + 1):
            counter = 0
            for n in nums:
                if n >= x:
                    counter += 1
            if counter == x:
                return counter
        return -1

print(Solution().specialArray(nums = [3,5]))
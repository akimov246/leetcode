import math

class Solution:
    def maxKelements(self, nums: list[int], k: int) -> int:

        def insert(n):
            if n <= nums[0]:
                nums.insert(0, n)
                return
            if n >= nums[-1]:
                nums.append(n)
                return
            left = 0
            right = len(nums)
            middle = (right + left) // 2
            while True:
                if nums[middle] <= n <= nums[middle + 1]:
                    nums.insert(middle + 1, n)
                    return
                elif nums[middle] < n:
                    left = middle + 1
                elif nums[middle] > n:
                    right = middle - 1
                middle = (right + left) // 2

        score = 0
        nums.sort()
        i = 0
        while i < k:
            current = nums.pop()
            insert(math.ceil(current / 3)) if nums else nums.append(math.ceil(current / 3))
            score += current
            i += 1

        return score


print(Solution().maxKelements(nums = [1,10,3,3,3], k = 3))
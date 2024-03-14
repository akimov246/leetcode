# Моё решение. Работает, но медленно.
class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        subarrays = 0
        left = 0
        right = 0
        next_one = -1
        while left < len(nums) and right < len(nums):
            if nums[left:right + 1].count(1) == goal:
                subarrays += 1
                if next_one != len(nums):
                    try:
                        next_one = nums.index(1, right + 1)
                    except:
                        next_one = len(nums)
                subarrays += next_one - (right + 1)
                right = next_one
            right += 1
            if right >= len(nums):
                left += 1
                right = left
        return subarrays

# Решение на префиксных суммах
class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        totalCount = 0
        currentSum = 0
        freq = {}

        for num in nums:
            currentSum += num
            if currentSum == goal:
                totalCount += 1

            if currentSum - goal in freq:
                totalCount += freq[currentSum - goal]

            freq[currentSum] = freq.get(currentSum, 0) + 1

        return totalCount



print(Solution().numSubarraysWithSum(nums = [1,0,1,0,1], goal = 2))

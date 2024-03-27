# Моё решение. Работает, но медленно
class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        subarrays = 0
        if k > 1 and all(n == 1 for n in set(nums)):
            tmp = 0
            for i in range(len(nums) + 1):
                tmp += i
            return tmp

        for i in range(len(nums)):
            res = 1
            for gap in range(i, len(nums)):
                res *= nums[gap]
                if res < k:
                    subarrays += 1
                else:
                    break

        return subarrays

# Решение с leetcode
class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        if k <= 1:
            return 0

        left, right, product, count = 0, 0, 1, 0
        n = len(nums)

        while right < n:
            product *= nums[right]
            while product >= k:
                product //= nums[left]
                left += 1
            count += 1 + (right - left)
            right += 1

        return count

print(Solution().numSubarrayProductLessThanK(nums = [10,5,2,6], k = 100))
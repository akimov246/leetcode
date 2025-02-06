from collections import defaultdict
from functools import cache

class Solution:
    def tupleSameProduct(self, nums: list[int]) -> int:
        result = 0
        products = defaultdict(set)
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                p = nums[i] * nums[j]
                products[p].update((nums[i], nums[j]))

        @cache
        def count_combinations(length):
            if length < 4:
                return 0
            # Сочетание
            n = length // 2
            k = 2
            #(factorial(n)//(factorial(n - k) * factorial(k))) * 8
            return 8 * n * (n - 1) // 2

        for value in products.values():
            result += count_combinations(len(value))

        return result

print(Solution().tupleSameProduct(nums = [2,3,4,6,8,12]))
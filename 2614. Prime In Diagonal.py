class Solution:
    def diagonalPrime(self, nums: list[list[int]]) -> int:

        def is_prime(num: int) -> bool:
            if num == 1:
                return False
            if num == 2:
                return True
            if num % 2 == 0:
                return False
            for x in range(3, int(num ** (1 / 2)) + 1, 2):
                if num % x == 0:
                    return False
            return True

        result = 0

        for i in range(len(nums)):
            if is_prime(nums[i][i]):
                result = max(result, nums[i][i])
            if is_prime(nums[i][(len(nums) - i - 1)]):
                result = max(result, nums[i][len(nums) - i - 1])
        return result

print(Solution().diagonalPrime(nums = [[1,2,3],[5,6,7],[9,10,11]]))
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        x = num // 2
        eps = 0.0000001
        while abs(x * x - num) > eps:
            x = (x + num / x) / 2
        return True if x - int(x) < eps else False

# Решение с Leetcode
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l, r = 0, num

        while l <= r:
            mid = l + (r - l) // 2

            if mid * mid == num:
                return True
            elif mid * mid > num:
                r = mid - 1
            else:
                l = mid + 1
        return False

print(Solution().isPerfectSquare(10000000124124124124))
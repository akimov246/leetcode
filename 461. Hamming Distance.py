class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x_bin = bin(x)[2:]
        y_bin = bin(y)[2:]
        length = len(max(x_bin, y_bin, key=len))
        x_bin = x_bin.rjust(length, '0')
        y_bin = y_bin.rjust(length, '0')
        ans = 0
        for i, j in zip(x_bin, y_bin):
            if i != j:
                ans += 1
        return ans

# Решение с Leetcode
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x^y).count('1')

print(Solution().hammingDistance(1, 4))
class Solution:
    def pivotInteger(self, n: int) -> int:
        left = sum(range(1, n + 1))
        right = 0
        x = n
        while x != -1:
            left -= x
            if left == right:
                return x
            right += x
            x -= 1
        return x

print(Solution().pivotInteger(8))
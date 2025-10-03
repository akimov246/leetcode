class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            product = 1
            for char in str(n):
                product *= int(char)
            if product % t == 0:
                return n
            n += 1


print(Solution().smallestNumber(n = 10, t = 2))
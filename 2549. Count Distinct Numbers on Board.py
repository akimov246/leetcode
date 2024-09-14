class Solution:
    def distinctIntegers(self, n: int) -> int:
        integers = set((n, ))
        while n:
            for i in range(1, n + 1):
                if n % i == 1:
                    integers.add(i)
            n -= 1
        return len(integers)

print(Solution().distinctIntegers(5))
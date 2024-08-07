class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        counter = 0
        for x in range(1, max(a, b) + 1):
            if a % x == 0 and b % x == 0:
                counter += 1
        return counter

print(Solution().commonFactors(12, 6))
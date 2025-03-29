class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        result = 0
        for i in range(limit + 1):
            for j in range(limit + 1):
                for k in range(limit + 1):
                    if i + j + k == n:
                        result += 1
        return result

print(Solution().distributeCandies(n = 5, limit = 2))
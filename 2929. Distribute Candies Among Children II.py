class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        counter = 0

        if True:
            for i in range(min(n, limit) + 1):
                rest = n - i
                if limit * 2 >= rest:
                    counter += min(rest, limit) + 1
                    counter -= max(0, rest - limit)

        return counter

#print(Solution().distributeCandies(n = 10001, limit = 20001)) # 50025003
#print(Solution().distributeCandies(n = 5, limit = 2))
#print(Solution().distributeCandies(n = 8444, limit = 6336))
#print(Solution().distributeCandies(n = 6, limit = 2))
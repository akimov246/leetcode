from functools import cache

class Solution:
    @cache
    def divisorGame(self, n: int) -> bool:
        if n == 1 or n == 3:
            return False
        if n == 2:
            return True

        divs = set()
        for i in range(1, n):
            if n % i == 0:
                divs.add(i)

        return any(self.divisorGame(d) for d in divs)



print(Solution().divisorGame(1025))
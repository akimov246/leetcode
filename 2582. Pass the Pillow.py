import itertools

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        for i in itertools.cycle(list(range(1, n + 1)) + list(range(n - 1, 1, -1))):
            if not time:
                return i
            time -= 1

print(Solution().passThePillow(n = 4, time = 5))
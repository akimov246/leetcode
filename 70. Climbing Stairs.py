class Solution:
    def climbStairs(self, n: int) -> int:
        result = 0
        if 1 == n:
            result += 1
        if n == 2:
            result += 1
        gen = self.rec(n, "1")
        for steps in gen:
            if sum(steps) == n:
                result += 1
        gen = self.rec(n, "2")
        for steps in gen:
            if sum(steps) == n:
                result += 1
        return result

    def rec(self, n, first):
        last = first
        while len(last) != n:
            yield [int(char) for char in list(last + "1")]
            yield [int(char) for char in list(last + "2")]
            last = last + first

#print(*Solution().rec(3, "1"))

print(Solution().climbStairs(4))


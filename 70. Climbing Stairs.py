import math
import time
import itertools

class Solution:

    def climbStairs(self, n: int) -> int:
        steps = [1 for i in range(n)]
        result = 0
        try:
            while True:
                permutations = math.factorial(len(steps)) // (math.factorial(steps.count(1)) * math.factorial(steps.count(2)))
                result += permutations
                steps.remove(1)
                steps.remove(1)
                steps.append(2)
        except:
            return result


    def mySlowClimbStairs(self, n: int) -> int:
        result = 0
        for steps in self.steps_generator(n):
            if sum(steps) == n:
                result += 1
        return result

    def steps_generator(self, n):
        power = 1
        while power < n:
            for i in range(2 ** power):
                l = list(str(bin(i))[2:].rjust(power, "0").replace("1", "2").replace("0", "1"))
                yield tuple(int(num) for num in l)
            power += 1
        yield tuple(1 for i in range(n))

start = time.perf_counter()
print(Solution().climbStairs(100))
print(time.perf_counter() - start)
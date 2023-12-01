class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:
            return True
        base = 3
        if n >= 0:
            values = set()
            res = 0
            pow = 0
            while res <= n:
                res = base ** pow
                values.add(res)
                if n / base in values:
                    return True
                n /= base
                pow += 1

        return False

print(Solution().isPowerOfThree(12523582682768786783462346823468234862983468342894689249868924986984621412412412412412412412412412412412))
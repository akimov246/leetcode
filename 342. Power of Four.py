class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 1:
            return True
        base = 4
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
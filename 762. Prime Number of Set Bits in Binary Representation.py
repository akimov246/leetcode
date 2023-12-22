class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        ans = 0
        for maybe_prime in (self.isPrimeFerma(bin(num).count("1")) for num in range(left, right + 1)):
            if maybe_prime:
                ans += 1
        return ans

    def isPrimeFerma(self, x: int, a = 2) -> bool:
        if x == 2:
            return True
        if a ** (x - 1) % x == 1:
            return True
        else:
            return False

print(Solution().countPrimeSetBits(6, 10))
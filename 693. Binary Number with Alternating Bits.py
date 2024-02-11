class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        if n == 0:
            return False
        if n == 1:
            return True
        if n < 0:
            raise ValueError('n не может быть отрицательным')
        n_bin = bin(n)[2:]
        prev = n_bin[0]
        for i in range(1, len(n_bin)):
            if prev == n_bin[i]:
                return False
            prev = n_bin[i]
        return True

print(Solution().hasAlternatingBits(7))
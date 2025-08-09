class Solution:
    def minChanges(self, n: int, k: int) -> int:
        n = bin(n)[2:]
        k = bin(k)[2:]
        n = n.rjust(len(max(n, k, key=len)), '0')
        k = k.rjust(len(max(n, k, key=len)), '0')
        #print(n, k)

        counter = 0
        for n_char, k_char in zip(n, k):
            if k_char == '1' and n_char == '0':
                return -1
            elif n_char != k_char:
                counter += 1

        return counter

print(Solution().minChanges(n = 14, k = 13))
from math import factorial

class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        if n == 1:
            return 1
        p = [2, 3, 5, 7]
        p_idx = 0
        prime = list(range(2, n + 1))
        while p_idx < len(p) and p[p_idx] ** 2 <= prime[-1]:
            for num in prime:
                if num % p[p_idx] == 0 and num != p[p_idx]:
                    prime.remove(num)
            p_idx += 1

        #print(prime)
        return factorial(len(prime)) * factorial(n - len(prime)) % (10 ** 9 + 7)



#print(Solution().numPrimeArrangements(4))
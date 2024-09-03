class Solution:
    def evenOddBit(self, n: int) -> list[int]:
        n = bin(n)[2:][::-1]
        even = 0
        odd = 0
        for i in range(len(n)):
            if n[i] == '1':
                if i % 2:
                    odd += 1
                else:
                    even += 1
        return [even, odd]

print(Solution().evenOddBit(50))
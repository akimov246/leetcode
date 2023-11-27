class Solution:
    def reverseBits(self, n: int) -> int:
        bits = bin(n)[2:].rjust(32, "0")
        return int(bits[::-1], 2)

print(Solution().reverseBits(43261596))
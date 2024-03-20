class Solution:
    def bitwiseComplement(self, n: int) -> int:
        return n ^ int('1' * len(bin(n)[2:]), 2)
        #return int(''.join([str(int(not bool(int(val)))) for val in n]), 2)

print(Solution().bitwiseComplement(5))
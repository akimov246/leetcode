class Solution:
    def findComplement(self, num: int) -> int:
        return int(''.join([str(int(not bool(int(char)))) for char in bin(num)[2:]]), 2)

print(Solution().findComplement(5))
class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        length_ones = 1
        while '1' * length_ones in s:
            length_ones += 1
        length_zeros = 1
        while '0' * length_zeros in s:
            length_zeros += 1
        return length_ones > length_zeros

print(Solution().checkZeroOnes(s = "1101"))
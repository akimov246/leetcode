class Solution:
    def alternateDigitSum(self, n: int) -> int:
        result = 0
        for i in range(len(str(n))):
            if i % 2 == 0:
                result += int(str(n)[i])
            else:
                result -= int(str(n)[i])
        return result

print(Solution().alternateDigitSum(521))
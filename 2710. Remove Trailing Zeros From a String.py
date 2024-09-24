class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        return str(int(num[::-1]))[::-1]

print(Solution().removeTrailingZeros(num = "51230100"))
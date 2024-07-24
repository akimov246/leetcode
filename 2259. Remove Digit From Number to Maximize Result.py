class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        max_ = 0
        for i in range(len(number)):
            if number[i] == digit:
                max_ = max(max_, int(number[:i] + number[i + 1:]))
        return str(max_)

print(Solution().removeDigit(number = "1231", digit = "1"))
import string

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        columnNumber -= 1
        letters = {i: char for i, char in enumerate(string.ascii_uppercase)}
        result = ""
        result += letters.get(columnNumber % len(letters))
        while columnNumber >= len(letters):
            columnNumber //= len(letters)
            columnNumber -= 1
            result += letters.get(columnNumber % len(letters))
        return result[::-1]

print(Solution().convertToTitle(27)) #"FXSHRXW"
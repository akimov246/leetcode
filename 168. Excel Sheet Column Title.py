import string

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        letters = {i: char for i, char in enumerate(string.ascii_uppercase, start=1)}
        result = ""
        while columnNumber > 0:
            result += letters.get(columnNumber % (len(letters)) + 1)
            columnNumber //= len(letters)
        return result

print(675 % 27)
print(Solution().convertToTitle(701))
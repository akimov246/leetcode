import string

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        letters = {char: i for i, char in enumerate(string.ascii_uppercase)}
        columnTitle = columnTitle[::-1]
        num = letters.get(columnTitle[0]) + 1
        columnTitle = columnTitle[1:]
        for i, char in enumerate(columnTitle, start=1):
            num += (letters.get(char) + 1) * (len(letters) ** i)
        return num



print(Solution().titleToNumber("FXSHRXW"))
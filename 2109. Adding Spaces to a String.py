class Solution:
    def addSpaces(self, s: str, spaces: list[int]) -> str:
        s = list(s)
        for space in spaces:
            s[space] = ' ' + s[space]
        return ''.join(s)

print(Solution().addSpaces(s = "LeetcodeHelpsMeLearn", spaces = [8,13,15]))
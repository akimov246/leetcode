class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        return ''.join(a if a < b else b for a, b in zip(s, s[::-1]))

print(Solution().makeSmallestPalindrome(s = "egcfe"))
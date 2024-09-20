class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if s == s[::-1]:
            return s
        for i in range(1, len(s)):
            if s[::-1][:i] + s == (s[::-1][:i] + s)[::-1]:
                return s[::-1][:i] + s
        return s

print(Solution().shortestPalindrome(s = "abbacd"))
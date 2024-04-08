class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if s == s[::-1]:
            return 1
        return 2

print(Solution().removePalindromeSub(s = "bbaabaaa"))
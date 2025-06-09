class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        for i in range(2, len(s) + 1):
            if s[i - 2:i] in s[::-1]:
                return True
        return False

print(Solution().isSubstringPresent(s = "leetcode"))
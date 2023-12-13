class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        i = 1
        while i != len(s):
            pattern = s[:i]
            post_pattern = s[i:i + i]
            if pattern != post_pattern:
                i += 1
            else:
                if s[:i] * (len(s) // len(pattern)) == s:
                    return True
                i += 1

        return False



print(Solution().repeatedSubstringPattern("abaababaab"))
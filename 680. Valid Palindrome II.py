class Solution:
    def validPalindrome(self, s: str) -> bool:

        def helper(s: str, count: int = 1):
            s_reversed = s[::-1]
            if s == s_reversed:
                return True
            for i in range(len(s)):
                if count:
                    if s[i] != s_reversed[i]:
                        s = s[:i] + s[i + 1:]
                        s_reversed = (s_reversed[:i] + s_reversed[i + 1:])[::-1]
                        return helper(s, 0) or helper(s_reversed, 0)
                else:
                    if s[i] != s_reversed[i]:
                        return False
            return True


        if s == s[::-1]:
            return True
        else:
            return helper(s, 1)

print(Solution().validPalindrome('abca'))
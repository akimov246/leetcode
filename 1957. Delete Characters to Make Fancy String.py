class Solution:
    def makeFancyString(self, s: str) -> str:
        ans = list(s[:2])
        for i in range(2, len(s)):
            #if any(char != s[i] for char in s[i-2:i]):
            if s[i] != s[i - 2] or s[i] != s[i - 1]:
                ans.append(s[i])
        return ''.join(ans)


print(Solution().makeFancyString(s = "aaabaaaa"))
class Solution:
    def removeDuplicates(self, s: str) -> str:
        if len(set(s)) == len(s):
            return s
        for i in range(len(s)):
            j = i + 1
            while j < len(s) and (s[j] == s[i]):
                j += 1
            if j - i > 1:
                s = s[:i] + s[j:]
                return self.removeDuplicates(s)




print(Solution().removeDuplicates(s = "aaaaaaaa"))
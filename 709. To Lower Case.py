import string

class Solution:
    def toLowerCase(self, s: str) -> str:
        #return s.lower()
        ans = ''
        upper = string.ascii_uppercase
        lower = string.ascii_lowercase
        for char in s:
            if char in upper:
                ans += lower[upper.index(char)]
            else:
                ans += char
        return ans

print(Solution().toLowerCase('Hello'))

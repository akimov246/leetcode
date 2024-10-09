class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        adds = 0

        while s:
            s = ''.join(s)
            while '()' in s:
                s = s.replace('()', '')
            s = list(s)
            if not s:
                return adds
            if s[0] == ')':
                s.insert(0, '(')
            elif s[0] == '(':
                s.insert(1, ')')
            adds += 1

        return adds

print(Solution().minAddToMakeValid(s = "()))(("))
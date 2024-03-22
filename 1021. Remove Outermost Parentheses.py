class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans = []
        open_parentheses = 0
        last = 0
        for i in range(len(s)):
            match s[i]:
                case '(':
                    open_parentheses += 1
                case ')':
                    open_parentheses -= 1
                    if not open_parentheses:
                        ans.append(s[last:i + 1][1:-1])
                        last = i + 1
        return "".join(ans)

print(Solution().removeOuterParentheses(s = "(()())(())"))
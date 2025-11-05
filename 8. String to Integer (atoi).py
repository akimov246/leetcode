class Solution:
    def myAtoi(self, s: str) -> int:
        digits = '0123456789'
        result = ''
        start = 0

        if not s:
            return 0

        while start < len(s) and s[start] == ' ':
            start += 1

        if start < len(s) and s[start] in ('-', '+'):
            result += f'{s[start]}0'
            start += 1

        while start < len(s) and s[start] == '0':
            start += 1

        for i in range(start, len(s)):
            if s[i] in digits:
                result += s[i]
            else:
                break

        if not result:
            return 0

        result = int(result)
        result = max(result, -2**31)
        result = min(result, 2**31 - 1)

        return result


print(Solution().myAtoi(s = "+-12"))
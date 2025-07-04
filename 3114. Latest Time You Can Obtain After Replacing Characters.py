class Solution:
    def findLatestTime(self, s: str) -> str:
        H = s[0]
        h = s[1]
        M = s[3]
        m = s[4]

        if H == '?':
            if h in ('0', '1', '?'):
                H = '1'
            else:
                H = '0'

        if h == '?':
            if H == '1':
                h = '1'
            else:
                h = '9'

        if M == '?':
            M = '5'

        if m == '?':
            m = '9'

        return f'{H}{h}:{M}{m}'

print(Solution().findLatestTime(s = "??:1?"))
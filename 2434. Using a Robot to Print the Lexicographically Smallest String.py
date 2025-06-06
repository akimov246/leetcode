class Solution:
    def robotWithString(self, s: str) -> str:
        p = ''
        t = ''
        minimal = []

        current = s[-1]
        for i in range(len(s) - 1, -1, -1):
            current = min(current, s[i])
            minimal.append(current)

        minimal.reverse()

        i = 0
        while i < len(s):
            if not t:
                t += s[i]
                i += 1
                continue
            if t[-1] <= minimal[i]:
                p += t[-1]
                t = t[:-1]
            else:
                t += s[i]
                i += 1


        return p + t[::-1]


print(Solution().robotWithString("mmuqezwmomeplrtskz"))
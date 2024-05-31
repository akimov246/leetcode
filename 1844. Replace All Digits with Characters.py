from string import ascii_lowercase

class Solution:
    def replaceDigits(self, s: str) -> str:
        def shift(c: str, x: int):
            c_idx = ascii_lowercase.index(c)
            return ascii_lowercase[c_idx + x]

        s = list(s)
        for i in range(1, len(s), 2):
            s[i] = shift(s[i - 1], int(s[i]))

        return ''.join(s)


print(Solution().replaceDigits(s = "a1c1e1"))
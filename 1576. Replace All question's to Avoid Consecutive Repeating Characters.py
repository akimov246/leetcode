from string import ascii_lowercase

class Solution:
    def modifyString(self, s: str) -> str:
        s = list(s)
        try:
            while True:
                index = s.index('?')
                invalid = set()
                if index != 0:
                    invalid.add(s[index - 1])
                if index != len(s) - 1:
                    invalid.add(s[index + 1])
                for char in ascii_lowercase:
                    if char not in invalid:
                        s[index] = char
                        break
        except ValueError:
            pass
        return ''.join(s)

print(Solution().modifyString(s = "?zs"))
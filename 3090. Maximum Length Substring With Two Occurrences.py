from collections import Counter

class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        result = 0
        l = 0
        r = 1

        def counter(string):
            c = {}
            for char in string:
                c[char] = c.get(char, 0) + 1
                if c[char] > 2:
                    return False
            return True

        while l < r and r < len(s) + 1:
            if counter(s[l:r]):
                result = max(result, r - l)
                r += 1
            else:
                l += 1

        return result

print(Solution().maximumLengthSubstring(s = "bcbbbcba"))
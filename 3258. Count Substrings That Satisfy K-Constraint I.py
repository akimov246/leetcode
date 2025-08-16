from functools import cache

class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        result = 0
        gap = 1

        @cache
        def count(chars):
            counter0 = 0
            counter1 = 0
            for c in chars:
                if c == '0':
                    counter0 += 1
                    if counter0 > k and counter1 > k:
                        return False
                else:
                    counter1 += 1
                    if counter0 > k and counter1 > k:
                        return False
            return True


        while gap <= len(s):
            for i in range(gap, len(s) + 1):
                result += count(s[i - gap:i])
            gap += 1

        return result


print(Solution().countKConstraintSubstrings(s = "1010101", k = 2))
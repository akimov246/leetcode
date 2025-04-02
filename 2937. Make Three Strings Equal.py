from itertools import zip_longest

class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        if s1 == s2 == s3:
            return 0
        for i, chars in enumerate(zip_longest(s1, s2, s3)):
            if len(set(chars)) != 1:
                if i == 0:
                    return -1
                return len(s1) - i + len(s2) - i + len(s3) - i
        return len(s1) - i + len(s2) - i + len(s3) - i

print(Solution().findMinimumOperations(s1 = "abc", s2 = "abb", s3 = "ab"))
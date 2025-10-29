class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        p = p.split('*')
        start = 0
        for pattern in p:
            start = s.find(pattern, start)
            if start != -1:
                start += len(pattern)
            else:
                break
        else:
            return True
        return False

print(Solution().hasMatch(s = "leetcode", p = "ee*e"))
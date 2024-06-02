class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        goods = 0
        for i in range(len(s) - 2):
            if len(s[i:i+3]) == len(set(s[i:i+3])):
                goods += 1
        return goods

print(Solution().countGoodSubstrings(s = "aababcabc"))
class Solution:
    def maxPower(self, s: str) -> int:
        power = 0
        n = 1
        for char in set(s):
            while s.find(char * n) != -1:
                power = max(power, n)
                n += 1
        return power

print(Solution().maxPower(s = "leetcode"))
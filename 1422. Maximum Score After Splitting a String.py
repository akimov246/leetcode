class Solution:
    def maxScore(self, s: str) -> int:
        score = 0
        for i in range(1, len(s)):
            left = s[:i].count('0')
            right = s[i:].count('1')
            score = max(score, left + right)
        return score


print(Solution().maxScore(s = "011101"))
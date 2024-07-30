class Solution:
    def minimumDeletions(self, s: str) -> int:
        if len(set(s)) == 1:
            return 0

        b_before = 0
        a_after = s.count('a')
        result = float('inf')
        for i in range(len(s)):
            if s[i] == 'a':
                a_after -= 1
            result = min(result, b_before + a_after)
            if s[i] == 'b':
                b_before += 1

        return result

print(Solution().minimumDeletions(s = "bbaaaaabb"))
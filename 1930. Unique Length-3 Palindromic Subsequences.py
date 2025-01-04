class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        result = 0
        seen = set()

        for i in range(len(s) - 2):
            if s[i] not in seen:
                seen.add(s[i])
                for j in range(len(s) - 1, i + 1, -1):
                    if s[i] == s[j]:
                        result += len(set(s[i + 1: j]))
                        break

        return result


print(Solution().countPalindromicSubsequence(s = "bbcbaba"))
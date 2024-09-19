class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        length = len(s)
        for _ in range(len(s)):
            if ('0' * (length // 2)) + ('1' * (length // 2)) in s:
                if length % 2:
                    length -= 1
                return length
            length -= 2
        else:
            return 0

print(Solution().findTheLongestBalancedSubstring(s = "01000111"))
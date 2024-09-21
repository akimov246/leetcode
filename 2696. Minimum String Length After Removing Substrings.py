class Solution:
    def minLength(self, s: str) -> int:
        prev = len(s)
        curr = None
        while prev != curr:
            prev = len(s)
            s = s.replace('AB', '')
            s = s.replace('CD', '')
            curr = len(s)
        return len(s)

print(Solution().minLength(s = "ABFCACDB"))
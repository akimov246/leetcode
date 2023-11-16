class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)


haystack = "sadbutsad"
needle = "gad"
print(Solution().strStr(haystack, needle))
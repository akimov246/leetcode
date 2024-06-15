class Solution:
    def isPrefixString(self, s: str, words: list[str]) -> bool:
        prefix = ''
        for word in words:
            prefix += word
            if len(prefix) > len(s):
                return False
            if prefix == s:
                return True
        return False

print(Solution().isPrefixString(s = "iloveleetcode", words = ["i","love","leetcode","apples"]))
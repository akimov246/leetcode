class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def is_nice(s: str):
            return all(char.swapcase() in s for char in set(s))

        length = len(s)
        while True:
            if length == 1:
                return ''
            for i in range(len(s)):
                sub_string = s[i:i + length]
                if is_nice(sub_string):
                    return sub_string
                if i + length == len(s):
                    length -= 1
                    break

print(Solution().longestNiceSubstring(s = "abcdefghijklmnopqrstuvwxyzAxaaA"))
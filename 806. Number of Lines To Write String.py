import math
import string

class Solution:
    def numberOfLines(self, widths: list[int], s: str) -> list[int]:
        char_width = {char: width for char, width in zip(string.ascii_lowercase, widths)}
        width = 0
        for char in s:
            if char_width[char] + width % 100 <= 100:
                width += char_width[char]
            else:
                width = width + (100 - width % 100)
                width += char_width[char]
        lines = math.ceil(width / 100)
        return [lines, width % 100 if width % 100 != 0 else 100]

print(Solution().numberOfLines(widths = [3,4,10,4,8,7,3,3,4,9,8,2,9,6,2,8,4,9,9,10,2,4,9,10,8,2], s = "mqblbtpvicqhbrejb"))
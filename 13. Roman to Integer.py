class Solution:

    DICT = {"I": 1,
               "V": 5,
               "X": 10,
               "L": 50,
               "C": 100,
               "D": 500,
               "M": 1000,
               }

    def romanToInt(self, s: str) -> int:
        dec_numbers = [self.DICT.get(char) for char in s[::-1]]
        prev = None
        result = 0
        for current in dec_numbers:
            if not prev:
                result += current
                prev = current
                continue
            if current < prev:
                result -= current
            else:
                result += current
            prev = current
        return result



print(Solution().romanToInt("LVIII"))
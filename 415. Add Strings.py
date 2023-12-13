from itertools import zip_longest

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        null = ord("0")
        if len(num1) >= len(num2):
            long = num1
            short = num2.rjust(len(long), "0")
        else:
            long = num2
            short = num1.rjust(len(long), "0")
        ans = ""
        in_mind = 0
        for l, s in zip_longest(long[::-1], short[::-1]):
            char_ord = ord(l) + ord(s) - null * 2 + in_mind
            if char_ord > 9:
                ans += str(char_ord)[-1]
                in_mind = 1
            else:
                ans += str(char_ord)
                in_mind = 0
        if in_mind == 1:
            ans += "1"
        return ans[::-1]

print(Solution().addStrings("999", '999'))
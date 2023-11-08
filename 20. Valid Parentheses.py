import random


class Solution:

    DICT = {
            "(": ")[{",
            ")": "()[]{}",
            "[": "]({",
            "]": "()[]{}",
            "{": "}([",
            "}": "()[]{}",
            }

    def isValid(self, s: str) -> bool:
        if (s.count("(") + s.count(")")) % 2 != 0:
            return False
        if (s.count("[") + s.count("]")) % 2 != 0:
            return False
        if (s.count("{") + s.count("}")) % 2 != 0:
            return False
        if s[-1] in "([{":
            return False
        if len(s) < 2:
            return False
        possible = "([{"
        for char in s:
            if char not in possible:
                return False
            possible = self.DICT.get(char)
        return True


print(Solution().isValid("()"))
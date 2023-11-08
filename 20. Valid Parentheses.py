import random


class Solution:

    DICT = {
            "(": "()[{",
            ")": "()[]{}",
            "[": "[]({",
            "]": "()[]{}",
            "{": "{}([",
            "}": "()[]{}",
            }

    def isValid(self, s: str) -> bool:
        if s[-1] in "([{":
            return False
        if len(s) % 2 != 0:
            return False
        possible = "([{"
        for char in s:
            if char not in possible:
                return False
            possible = self.DICT.get(char)

        s = list(s)
        while True:
            try:
                if len(s) == 0:
                    return True
                char = s[0]
                match char:
                    case "("|")":
                        s.remove("(")
                        s.remove(")")
                    case "["|"]":
                        s.remove("[")
                        s.remove("]")
                    case "{"|"}":
                        s.remove("{")
                        s.remove("}")
                    case _:
                        return False
            except:
                return False


print(Solution().isValid("[([]])"))
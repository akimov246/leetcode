import random


class Solution:

    def isValid(self, s: str) -> bool:
        if s[0] in ")]}" or s[-1] in "([{":
            return False
        should = []
        for char in s:
            match char:
                case "(":
                    should.append(")")
                case "[":
                    should.append("]")
                case "{":
                    should.append("}")
                case _:
                    if char not in should:
                        return False
                    if should[-1] != char:
                        return False
                    should.pop()

        return not bool(len(should))


print(Solution().isValid("[([]])"))
                         #}
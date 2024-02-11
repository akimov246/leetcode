import re

class Solution:
    def calPoints(self, operations: list[str]) -> int:

        def isint(s):
            return bool(re.match('[-+]?\d+', s))

        stack = []
        operations = [int(ops) if isint(ops) else ops for ops in operations]
        for ops in operations:
            match ops:
                case int():
                    stack.append(ops)
                case '+':
                    stack.append(stack[-1] + stack[-2])
                case 'D':
                    stack.append(stack[-1] * 2)
                case 'C':
                    stack.pop()
        return sum(stack)

print(Solution().calPoints(operations = ["5","-2","4","C","D","9","+","+"]))
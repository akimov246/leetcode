import decimal

class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for t in tokens:
            match t:
                case '+':
                    stack.append(stack.pop() + stack.pop())
                case '-':
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(a - b)
                case '*':
                    stack.append(stack.pop() * stack.pop())
                case '/':
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(int(a / b))
                case _:
                    if isinstance(int(t), int):
                        stack.append(int(t))

        return stack[0]

print(Solution().evalRPN(tokens = ["0","3","/"]))
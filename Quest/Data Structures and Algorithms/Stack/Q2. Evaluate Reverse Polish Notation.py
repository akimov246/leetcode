class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        operators = "+-*/"
        stack = []

        for token in tokens:
            if token in operators:
                b = stack.pop()
                a = stack.pop()
                stack.append(str(int(eval(a + token + b))))
            else:
                stack.append(token)

        return int(stack[0])


print(Solution().evalRPN(tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
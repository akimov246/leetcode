class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []
        for char in s:
            match char:
                case '(' | '*':
                    stack.append(char)
                case ')':
                    if not stack:
                        return False
                    if '(' in stack:
                        stack.reverse()
                        stack.pop(stack.index('('))
                        stack.reverse()
                    else:
                        stack.pop()

        for i in range(len(stack) - 1, -1, -1):
            if stack[i] == '(':
                try:
                    stack.pop(i + 1)
                    stack.pop(i)
                except:
                    return False

        return not stack or ('(' not in stack and ')' not in stack)

print(Solution().checkValidString("(()(())()())*((()(())))*()(*)()()(*((()((*(*))))()*()(()((()(*((()))*(((())(())))*))(()*))(()*)"))

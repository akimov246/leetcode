class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack_s = []
        stack_t = []
        for char in s:
            if char == '#':
                try:
                    stack_s.pop()
                except IndexError:
                    pass
                continue
            stack_s.append(char)
        for char in t:
            if char == '#':
                try:
                    stack_t.pop()
                except IndexError:
                    pass
                continue
            stack_t.append(char)

        return stack_s == stack_t



print(Solution().backspaceCompare(s = "ab#c", t = "ad#c"))
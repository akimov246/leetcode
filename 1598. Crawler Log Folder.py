class Solution:
    def minOperations(self, logs: list[str]) -> int:
        stack = []
        for operation in logs:
            match operation:
                case './':
                    pass
                case '../':
                    if stack:
                        stack.pop()
                case _:
                    stack.append(operation)
        return len(stack)

print(Solution().minOperations(logs = ["d1/","d2/","../","d21/","./"]))
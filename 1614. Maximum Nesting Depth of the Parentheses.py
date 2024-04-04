class Solution:
    def maxDepth(self, s: str) -> int:
        depth = 0
        current = 0
        for char in s:
            match char:
                case '(':
                    current += 1
                    depth = max(depth, current)
                case ')':
                    current -= 1
                    depth = max(depth, current)
        return depth


print(Solution().maxDepth(s = "(1+(2*3)+((8)/4))+1"))
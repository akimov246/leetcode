class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if s == goal:
            return True

        def left_shift(s):
            return s[1:] + s[0]

        for i in range(len(s) - 1):
            s = left_shift(s)
            if s  == goal:
                return True
        return False

print(Solution().rotateString(s = "gcmbf", goal = "fgcmb"))
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        if set(s) != set(goal):
            return False
        if s == goal and len(set(s)) == len(s) == len(set(goal)) == len(goal):
            return False

        diff_s = []
        diff_goal = []
        for char_s, char_goal in zip(s, goal):
            if char_s != char_goal:
                diff_s.append(char_s)
                diff_goal.append(char_goal)

        if not diff_s:
            return True

        left = 0
        right = 1

        while left < len(diff_s) and right < len(diff_s):
            diff_s[left], diff_s[right] = diff_s[right], diff_s[left]
            if diff_s == diff_goal:
                return True
            diff_s[left], diff_s[right] = diff_s[right], diff_s[left]
            right += 1
            if right >= len(diff_s):
                left += 1
                right = left + 1

        return False

print(Solution().buddyStrings(s = "aa", goal = "aa"))

class Solution:
    def firstUniqChar(self, s: str) -> int:
        for char in s:
            if self.my_count(s, char):
                return s.index(char)
        return -1

    def my_count(self, s, c):
        ans = 0
        for char in s:
            if char == c:
                ans += 1
                if ans > 1:
                    return False
        return True

print(Solution().firstUniqChar("aabb"))
class Solution:
    def largeGroupPositions(self, s: str) -> list[list[int]]:
        large = []
        start = 0
        end = 0

        while start < len(s) and end < len(s):
            if s[start] == s[end]:
                end += 1
                if end == len(s):
                    if end - start >= 3:
                        large.append([start, end - 1])
            else:
                if end - start >= 3:
                    large.append([start, end - 1])
                start = end

        return large


print(Solution().largeGroupPositions(s = "abbxxxxzzyууу"))
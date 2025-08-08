class Solution:
    def numberOfAlternatingGroups(self, colors: list[int]) -> int:
        result = 0
        colors.extend(colors[:2])

        for i in range(1, len(colors) - 1):
            if colors[i - 1] != colors[i] != colors[i + 1]:
                result += 1

        return result

print(Solution().numberOfAlternatingGroups(colors = [0,1,0,0,1]))
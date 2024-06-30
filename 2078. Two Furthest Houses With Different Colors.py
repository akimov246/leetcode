class Solution:
    def maxDistance(self, colors: list[int]) -> int:
        max_distance = 0
        for i in range(len(colors)):
            for j in range(len(colors) - 1, i, -1):
                if colors[i] != colors[j]:
                    max_distance = max(max_distance, j - i)
                    break
        return max_distance

print(Solution().maxDistance(colors = [4,4,4,11,4,4,11,4,4,4,4,4]))
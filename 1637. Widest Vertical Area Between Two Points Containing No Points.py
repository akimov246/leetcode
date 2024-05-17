class Solution:
    def maxWidthOfVerticalArea(self, points: list[list[int]]) -> int:
        xes = sorted(set([coord[0] for coord in points]))
        max_ = 0
        for i in range(1, len(xes)):
            max_ = max(max_, xes[i] - xes[i - 1])
        return max_

print(Solution().maxWidthOfVerticalArea(points = [[8,7],[9,9],[7,4],[9,7]]))
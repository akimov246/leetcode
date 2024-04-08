class Solution:
    def minTimeToVisitAllPoints(self, points: list[list[int]]) -> int:
        time = 0
        for i in range(1, len(points)):
            x_prev = points[i - 1][0]
            y_prev = points[i - 1][1]
            x = points[i][0]
            y = points[i][1]
            time += max(abs(x - x_prev), abs(y - y_prev))
        return time

print(Solution().minTimeToVisitAllPoints(points = [[1,1],[3,4],[-1,0]]))
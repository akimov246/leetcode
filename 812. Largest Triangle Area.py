class Solution:
    def largestTriangleArea(self, points: list[list[int]]) -> float:
        #Area = (1/2) * |x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)|
        area = 0
        for i in range(len(points)):
            for j in range(len(points)):
                for k in range(len(points)):
                    if i != j != k:
                        area = max(area, 1/2*abs(points[i][0]*(points[j][1] - points[k][1]) + \
                                          points[j][0]*(points[k][1] - points[i][1]) + \
                                          points[k][0]*(points[i][1] - points[j][1])))

        return area

print(Solution().largestTriangleArea(points = [[8,10],[2,7],[9,2],[4,10]]))
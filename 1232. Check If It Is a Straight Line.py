class Solution:
    def checkStraightLine(self, coordinates: list[list[int]]) -> bool:
        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]
        y2_y1 = y2 - y1
        x2_x1 = x2 -x1
        for i in range(2, len(coordinates)):
            x3, y3 = coordinates[i]
            if y2_y1 * (x3 - x2) != (y3 - y2) * x2_x1:
                return False
        return True

print(Solution().checkStraightLine(coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]))
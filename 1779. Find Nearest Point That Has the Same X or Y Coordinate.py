class Solution:
    def nearestValidPoint(self, x: int, y: int, points: list[list[int]]) -> int:
        index = -1
        min_distance = float('inf')
        for i, (a, b) in enumerate(points):
            if x == a or y == b:
                distance = abs(x - a) + abs(y - b)
                if distance < min_distance:
                    min_distance = distance
                    index = i
        return index


print(Solution().nearestValidPoint(x = 3, y = 4, points = [[1,2],[3,1],[2,4],[2,3],[4,4]]))
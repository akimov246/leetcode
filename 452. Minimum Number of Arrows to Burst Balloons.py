class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        if len(points) == 1:
            return 1
        arrows = 0
        burst = set()
        #points = sorted(points, key=lambda item: (item[0], item[1]))
        points = sorted(points, key=lambda item: item[0])
        for i, baloon in enumerate(points):
            if tuple(baloon) not in burst:
                burst.add(tuple(baloon))
                arrows += 1
                start = baloon[0]
                end = baloon[1]
                for j in range(i + 1, len(points)):
                    s = points[j][0]
                    e = points[j][1]

                    a = max(start, s)
                    b = min(end, e)
                    if a <= b:
                        start = a
                        end = b
                        if (points[j][0], points[j][1]) not in burst:
                            burst.add((points[j][0], points[j][1]))
                    else:
                        break

        return arrows

print(Solution().findMinArrowShots([[3,9],[7,12],[3,8],[6,8],[9,10],[2,9],[0,9],[3,9],[0,6],[2,8]]))
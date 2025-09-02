class Solution:
    def numberOfPairs(self, points: list[list[int]]) -> int:
        count = 0
        points.sort(key=lambda item: (item[0], -item[1]), reverse=True)

        for i in range(len(points) - 1):
            for j in range(i + 1, len(points)):
                if points[i][0] >= points[j][0] and points[i][1] <= points[j][1]:
                    if j - i - 1 == 0:
                        count += 1
                        continue
                    for m in range(i + 1, j):
                        if points[j][0] <= points[m][0] <= points[i][0] and points[i][1] <= points[m][1] <= points[j][1]:
                            break
                    else:
                        count += 1

        return count

print(Solution().numberOfPairs(points = [[0,1],[0,2],[2,5],[3,0]]))
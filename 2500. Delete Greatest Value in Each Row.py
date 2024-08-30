class Solution:
    def deleteGreatestValue(self, grid: list[list[int]]) -> int:
        answer = 0
        while grid[0]:
            max_ = 0
            for row in grid:
                m = max(row)
                row.remove(m)
                max_ = max(max_, m)
            answer += max_
        return answer


print(Solution().deleteGreatestValue(grid = [[1,2,4],[3,3,1]]))
from copy import deepcopy

class Solution:
    def modifiedMatrix(self, matrix: list[list[int]]) -> list[list[int]]:
        answer = deepcopy(matrix)
        max_value_of_col = []
        for col in zip(*matrix):
            max_value_of_col.append(max(col))

        for i in range(len(answer)):
            for j in range(len(answer[0])):
                if answer[i][j] == -1:
                    answer[i][j] = max_value_of_col[j]

        return answer

print(Solution().modifiedMatrix(matrix = [[2,-1,2,-1,2],[1,0,-1,2,-1],[2,-1,-1,-1,2],[2,1,2,-1,2],[0,1,0,0,0],[0,0,0,0,-1],[2,-1,2,2,0],[0,1,0,2,2],[2,2,0,1,-1]]))
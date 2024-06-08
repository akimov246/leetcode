class Solution:
    def findRotation(self, mat: list[list[int]], target: list[list[int]]) -> bool:
        if mat == target:
            return True
        tmp = []
        for _ in range(3):
            for m in zip(*mat):
                tmp.append(list(m[::-1]))
            if tmp == target:
                return True
            mat = tmp.copy()
            tmp.clear()
        return False

print(Solution().findRotation([[0,0,0],[0,0,1],[0,0,1]], target = [[0,0,0],[0,0,1],[0,0,1]]))
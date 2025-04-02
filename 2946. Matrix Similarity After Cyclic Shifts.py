class Solution:
    def areSimilar(self, mat: list[list[int]], k: int) -> bool:
        init_mat = mat.copy()
        for _ in range(k):
            for i in range(len(mat)):
                if i % 2:
                    mat[i] = [mat[i][-1]] + mat[i][:-1]
                else:
                    mat[i] = mat[i][1:] + [mat[i][0]]

        return init_mat == mat

print(Solution().areSimilar(mat = [[1,2,1,2],[5,5,5,5],[6,3,6,3]], k = 2))
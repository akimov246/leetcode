class Solution:
    def kWeakestRows(self, mat: list[list[int]], k: int) -> list[int]:
        def my_sort(row):
            return row.count(1)

        sorted_mat = sorted(mat, key=my_sort)[:k]
        ans = []
        for row in sorted_mat:
            start = 0
            while True:
                index = mat.index(row, start)
                if index not in ans:
                    ans.append(index)
                    break
                start = index + 1
        return ans


print(Solution().kWeakestRows(mat =
[[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]],
k = 3))
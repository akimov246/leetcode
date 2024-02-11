class Solution:
    def imageSmoother(self, img: list[list[int]]) -> list[list[int]]:

        def get_cell_surround_avg(img, x, y):
            avg = 0
            number_of_cells = 0
            surround_coords = ((-1, 1), (0, 1), (1, 1),
                               (-1, 0), (0, 0), (1, 0),
                               (-1,-1), (0,-1), (1,-1))
            #surround_coords = ((x, y) for x in (-1, 0, 1) for y in (-1, 0, 1))
            for h, v in surround_coords:
                if x + h >= 0 and y + v >= 0 and x + h < len(img) and y + v < len(img[0]):
                    avg += img[x + h][y + v]
                    number_of_cells += 1
            return avg // number_of_cells

        ans = [[None] * len(img[0]) for _ in range(len(img))]

        for i in range(len(img)):
            for j in range(len(img[i])):
                ans[i][j] = get_cell_surround_avg(img, i, j)

        return ans

print(Solution().imageSmoother(img = [[2,3,4],[5,6,7],[8,9,10],[11,12,13],[14,15,16]]))


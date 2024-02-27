class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        for i in range(len(image)):
            image[i].reverse()
            image[i] = [int(not value) for value in image[i]]
        return image

print(Solution().flipAndInvertImage(image = [[1,1,0],[1,0,1],[0,0,0]]))
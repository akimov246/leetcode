class Solution:

    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        pixels_to_fill = set(((sr, sc), ))

        def helper(image, sr, sc):
            nonlocal pixels_to_fill
            buffer = set()
            if sr - 1 in range(0, len(image)) and image[sr][sc] == image[sr - 1][sc] and (sr - 1, sc) not in pixels_to_fill:
                buffer.add((sr - 1, sc))
            if sr + 1 in range(0, len(image)) and image[sr][sc] == image[sr + 1][sc] and (sr + 1, sc) not in pixels_to_fill:
                buffer.add((sr + 1, sc))
            if sc - 1 in range(0, len(image[0])) and image[sr][sc] == image[sr][sc - 1] and (sr, sc - 1) not in pixels_to_fill:
                buffer.add((sr, sc - 1))
            if sc + 1 in range(0, len(image[0])) and image[sr][sc] == image[sr][sc + 1] and (sr, sc + 1) not in pixels_to_fill:
                buffer.add((sr, sc + 1))
            pixels_to_fill.update(buffer)
            for sr, sc in buffer:
                helper(image, sr, sc)

        helper(image, sr, sc)
        for sr, sc in pixels_to_fill:
            image[sr][sc] = color

        return image

print(Solution().floodFill([[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0))
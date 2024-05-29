class Solution:
    def countGoodRectangles(self, rectangles: list[list[int]]) -> int:
        squares_lengths = {}
        for l, w in rectangles:
            square_length = min(l, w)
            squares_lengths[square_length] = squares_lengths.get(square_length, 0) + 1
        return squares_lengths[max(squares_lengths)]

print(Solution().countGoodRectangles(rectangles = [[5,8],[3,9],[5,12],[16,5]]))
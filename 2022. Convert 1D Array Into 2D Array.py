class Solution:
    def construct2DArray(self, original: list[int], m: int, n: int) -> list[list[int]]:

        if m * n != len(original):
            return []

        def get_one_element_gen(arr: list[int]):
            yield from arr

        element = get_one_element_gen(original)

        matrix = []
        for i in range(m):
            matrix.append([])
            for _ in range(n):
                try:
                    matrix[i].append(next(element))
                except:
                    break

        return matrix

print(Solution().construct2DArray(original = [1,2,3,4], m = 2, n = 2))
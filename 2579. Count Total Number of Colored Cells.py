class Solution:
    def coloredCells(self, n: int) -> int:
        def helper(n):
            counter = 1
            result = 1
            while counter != n + 1:
                result = result + 4 * (counter - 1)
                counter += 1
            return result

        return helper(n)

print(Solution().coloredCells(1488))
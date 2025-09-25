class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:

        dp = []
        for i in range(len(triangle)):
            dp.append([None] * len(triangle[-1]))
        dp[0][0] = triangle[0][0]
        #print(dp)

        def helper(i, j):
            if i == 0 and j == 0:
                return dp[0][0]
            if i < 0 or j < 0 or j >= len(triangle[i]):
                return float('inf')
            if dp[i - 1][j] is None:
                dp[i - 1][j] = helper(i - 1, j)
            if dp[i - 1][j - 1] is None:
                dp[i - 1][j - 1] = helper(i - 1, j - 1)
            dp[i][j] = triangle[i][j] + min(dp[i - 1][j], dp[i - 1][j - 1])
            return dp[i][j]

        result = float('inf')
        for j in range(len(triangle[-1])):
            result = min(result, helper(len(triangle) - 1, j))

        return result


print(Solution().minimumTotal(triangle = [[-10]]))
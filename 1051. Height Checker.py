class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        ans = 0
        expected = sorted(heights)
        for h, e in zip(heights, expected):
            if h != e:
                ans += 1
        return ans

print(Solution().heightChecker(heights = [1,1,4,2,1,3]))
class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        g = tuple(sorted(g))
        s = tuple(sorted(s))
        ans = 0
        cookie = 0
        child = 0
        while cookie < len(s) and child < len(g):
            if s[cookie] >= g[child]:
                ans += 1
                cookie += 1
                child += 1
            else:
                cookie += 1
        return ans

print(Solution().findContentChildren([1,2], [1,2,3]))
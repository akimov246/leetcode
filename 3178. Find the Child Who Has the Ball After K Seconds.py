class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        children = list(range(n))
        add = children[:-1][::-1] + children[1:]
        while len(children) <= 50:
            children += add

        return children[k]

print(Solution().numberOfChild(n = 3, k = 5))
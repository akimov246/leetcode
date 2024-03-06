class Solution:
    def hasGroupsSizeX(self, deck: list[int]) -> bool:
        groups = dict().fromkeys(set(deck), 0)
        for x in deck:
            groups[x] += 1
        values = set(groups.values())
        if 1 in values:
            return False
        min_ = min(values)
        start = 2 if min_ % 2 == 0 else 3
        for i in range(start, min_ + 1):
            if all(c % i == 0 for c in values):
                return True
        return False



print(Solution().hasGroupsSizeX(deck = [1,1]))
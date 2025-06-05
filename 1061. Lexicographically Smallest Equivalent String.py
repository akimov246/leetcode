from collections import defaultdict

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        equivalents = defaultdict(set)

        for a, b in zip(s1, s2):
            if a != b:
                equivalents[a].add(b)
                equivalents[b].add(a)

        cache = {}

        def helper(key, checked=None):
            if checked is None:
                checked = set()
            checked.add(key)
            for value in equivalents[key]:
                if value not in checked:
                    helper(value, checked)
            return min(checked)

        result = ''
        for letter in baseStr:
            if not cache.get(letter):
                cache[letter] = helper(letter)
            result += cache[letter]

        return result


print(Solution().smallestEquivalentString(s1 = "leetcode", s2 = "programs", baseStr = "sourcecode"))
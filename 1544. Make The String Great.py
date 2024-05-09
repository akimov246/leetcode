class Solution:
    def makeGood(self, s: str) -> str:

        def helper(s: str):
            to_remove = set()
            for char in set(s):
                if char.isupper():
                    to_remove.add(char + char.lower())
                    to_remove.add(char.lower() + char)
            if any(element in s for element in to_remove):
                for element in to_remove:
                    s = s.replace(element, '')
                return helper(s)
            else:
                return s

        return helper(s)


print(Solution().makeGood(s = 'aAbBBBBbbbbBBBbbbBBBBbbbbbBBBBBBBBBbb'))
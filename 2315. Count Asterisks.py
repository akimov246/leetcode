class Solution:
    def countAsterisks(self, s: str) -> int:
        counter = 0
        for i, part in enumerate(s.split('|')):
            if i % 2 == 0:
                counter += part.count('*')
        return counter

print(Solution().countAsterisks(s = "l|*e*et|c**o|*de|"))
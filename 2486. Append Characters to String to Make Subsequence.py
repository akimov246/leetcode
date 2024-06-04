class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        counter = len(t)
        start = 0
        for char in t:
            start = s.find(char, start) + 1
            if not start:
                break
            counter -= 1
        return counter

print(Solution().appendCharacters(s = "coaching", t = "coding"))
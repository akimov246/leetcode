class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        set_s1 = set(s1)

        def counter(s):
            d = {}
            for char in s:
                d[char] = d.get(char, 0) + 1
            return d

        counter_s1 = counter(s1)

        for i in range(n, len(s2) + 1):
            if set_s1 == set(s2[i - n:i]):
                counter_s2 = counter(s2[i - n:i])
                if counter_s1 == counter_s2:
                    return True

        return False

print(Solution().checkInclusion(s1 = "heolo", s2 = "ooolleoooleh"))
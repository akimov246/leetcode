class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        return list((set((s1[0], s1[2])), set((s1[1], s1[3])))) == list((set((s2[0], s2[2])), set((s2[1], s2[3]))))

print(Solution().canBeEqual(s1 = "abcd", s2 = "cdab"))
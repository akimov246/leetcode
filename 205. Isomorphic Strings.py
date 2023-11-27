class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        unic_s = list(dict.fromkeys(s).keys())
        unic_t = list(dict.fromkeys(t).keys())

        for char_s, char_t in zip(s, t):
            if unic_s.index(char_s) != unic_t.index(char_t):
                return False
        return True


print(Solution().isIsomorphic("foo", "bar"))
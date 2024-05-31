class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        if set(s1) != set(s2):
            return False
        s1 = list(s1)
        s2 = list(s2)
        for i1, (char1, char2) in enumerate(zip(s1, s2)):
            if char1 != char2:
                begin = 0
                while True:
                    try:
                        i2 = s2.index(char1, begin)
                        s2[i1], s2[i2] = s2[i2], s2[i1]
                        if s1 == s2:
                            return True
                        else:
                            s2[i1], s2[i2] = s2[i2], s2[i1]
                            begin = i2 + 1
                    except:
                        return False


print(Solution().areAlmostEqual(s1 = "ysmpagrkzsmmzmsssutzgpxrmoylkgemgfcperptsxjcsgojwourhxlhqkxumonfgrczmjvbhwvhpnocz",
                                s2 = "ysmpagrqzsmmzmsssutzgpxrmoylkgemgfcperptsxjcsgojwourhxlhkkxumonfgrczmjvbhwvhpnocz"))
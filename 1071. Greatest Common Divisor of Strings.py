class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        divisor = min(str1, str2, key=len)

        def check(s, d):
            div = d
            while True:
                if div == s:
                    return True
                if len(div) < len(s):
                    div += d
                else:
                    return False

        while True:
            if check(str1, divisor) and check(str2, divisor):
                return divisor
            divisor = divisor[:-1]
            if not divisor:
                return divisor




print(Solution().gcdOfStrings(str1 = "LEET", str2 = "CODE"))
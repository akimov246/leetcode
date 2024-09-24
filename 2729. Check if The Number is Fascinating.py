class Solution:
    def isFascinating(self, n: int) -> bool:
        n = str(n) + str(n * 2) + str(n * 3)
        if '0' in n or len(n) > len(set(n)):
            return False
        return True

print(Solution().isFascinating(111))
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = bin(a)
        print(a)

a = "11"
b = "1"
print(Solution().addBinary(a, b))
class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        s = "".join([str(num) for num in digits])
        s = str(int(s) + 1)
        d = [int(char) for char in list(s)]
        return d


digits = [1, 2, 3]
print(Solution().plusOne(digits))
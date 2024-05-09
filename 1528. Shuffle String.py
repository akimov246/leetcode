class Solution:
    def restoreString(self, s: str, indices: list[int]) -> str:
        result = [None] * len(s)
        for char, index in zip(s, indices):
            result[index] = char
        return ''.join(result)

print(Solution().restoreString(s = "codeleet", indices = [4,5,6,7,0,2,1,3]))
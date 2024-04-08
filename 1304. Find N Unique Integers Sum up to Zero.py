class Solution:
    def sumZero(self, n: int) -> list[int]:
        array = []
        if n % 2:
            array.append(0)
        i = 1
        while len(array) != n:
            array.extend([i, -i])
            i += 1
        return array

print(Solution().sumZero(4))
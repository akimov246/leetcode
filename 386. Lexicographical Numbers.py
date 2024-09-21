class Solution:
    def lexicalOrder(self, n: int) -> list[int]:
        return sorted(list(range(1, n + 1)), key=lambda value: tuple(str(value)))

print(Solution().lexicalOrder(14888))
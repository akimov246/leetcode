class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        index = k
        operations = blocks[:k].count('W')
        current = operations
        while index != len(blocks):
            if blocks[index - k] == 'W':
                current -= 1
            if blocks[index] == 'W':
                current += 1
            operations = min(operations, current)
            index += 1

        return operations

print(Solution().minimumRecolors(blocks = "WBB", k = 1))
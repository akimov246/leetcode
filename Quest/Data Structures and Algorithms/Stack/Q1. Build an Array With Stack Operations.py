class Solution:
    def buildArray(self, target: list[int], n: int) -> list[str]:
        operations: list[str] = []
        target_idx: int = 0

        for value in range(1, n + 1):
            if target_idx >= len(target):
                break
            operations.append('Push')
            if value == target[target_idx]:
                target_idx += 1
            else:
                operations.append('Pop')

        return operations


print(Solution().buildArray(target = [1,3], n = 3))
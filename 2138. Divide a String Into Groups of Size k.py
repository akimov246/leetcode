class Solution:
    def divideString(self, s: str, k: int, fill: str) -> list[str]:
        groups = []
        for i in range(0, len(s), k):
            if len(s[i:i+k]) == k:
                groups.append(s[i:i+k])
            else:
                groups.append(f'{s[i:i+k]:{fill}<{k}}')
        return groups

print(Solution().divideString(s = "abcdefghij", k = 3, fill = "x"))
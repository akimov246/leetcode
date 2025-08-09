class Solution:
    def getSmallestString(self, s: str) -> str:
        result = list(s)
        for i in range(1, len(result)):
            if int(result[i]) % 2 == int(result[i - 1]) % 2:
                if result[i] < result[i - 1]:
                    result[i], result[i - 1] = result[i - 1], result[i]
                    break
        return ''.join(result)

print(Solution().getSmallestString(s = "45320"))
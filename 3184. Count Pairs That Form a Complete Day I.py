class Solution:
    def countCompleteDayPairs(self, hours: list[int]) -> int:
        result = 0
        for i in range(len(hours)):
            for j in range(i + 1, len(hours)):
                if (hours[i] + hours[j]) % 24 == 0:
                    result += 1

        return result

print(Solution().countCompleteDayPairs(hours = [12,12,30,24,24]))
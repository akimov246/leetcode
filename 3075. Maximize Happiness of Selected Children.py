class Solution:
    def maximumHappinessSum(self, happiness: list[int], k: int) -> int:
        result = 0
        happiness.sort(reverse=True)
        for i in range(k):
            value = happiness[i] - i
            if value > 0:
                result += value
            else:
                break

        return result

print(Solution().maximumHappinessSum(happiness = [12,1,42], k = 3))
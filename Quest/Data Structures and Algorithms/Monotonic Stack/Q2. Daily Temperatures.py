class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        answer = [None] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                j = stack.pop()
                answer[j] = i - j
            stack.append(i)

        for s in stack:
            answer[s] = 0

        return answer


print(Solution().dailyTemperatures(temperatures = [73,74,75,71,69,72,76,73]))
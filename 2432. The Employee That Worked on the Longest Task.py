class Solution:
    def hardestWorker(self, n: int, logs: list[list[int]]) -> int:
        id = logs[0][0]
        longest_time = logs[0][1]
        for i in range(1, len(logs)):
            if logs[i][1] - logs[i - 1][1] > longest_time:
                longest_time = logs[i][1] - logs[i - 1][1]
                id = logs[i][0]
            elif logs[i][1] - logs[i - 1][1] == longest_time:
                id = min(id, logs[i][0])

        return id

print(Solution().hardestWorker(n = 70, logs = [[36,3],[1,5],[12,8],[25,9],[53,11],[29,12],[52,14]]))
class Solution:
    def exclusiveTime(self, n: int, logs: list[str]) -> list[int]:
        executed_functions = []
        exclusive_time = {}
        current_time = 0

        for log in logs:
            id, state, timestamp = log.split(':')
            id = int(id)
            timestamp = int(timestamp)
            if state == "start":
                if executed_functions:
                    exclusive_time[executed_functions[-1]] = exclusive_time.get(executed_functions[-1], 0) + timestamp - current_time
                executed_functions.append(id)
            else:
                timestamp = timestamp + 1
                exclusive_time[id] = exclusive_time.get(id, 0) + timestamp - current_time
                executed_functions.pop()
            current_time = timestamp

        return list(exclusive_time.values())

print(Solution().exclusiveTime(n = 1, logs = ["0:start:0","0:start:2","0:end:5","0:start:6","0:end:6","0:end:7"]))
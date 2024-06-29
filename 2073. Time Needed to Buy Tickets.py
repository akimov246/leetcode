class Solution:
    def timeRequiredToBuy(self, tickets: list[int], k: int) -> int:
        time = 0
        while True:
            for i in range(len(tickets)):
                #dbg = tickets[i]
                if tickets[i]:
                    tickets[i] -= 1
                    time += 1
                if i == k and not tickets[i]:
                    return time

print(Solution().timeRequiredToBuy(tickets = [2,3,2], k = 2))
class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        richman = 0
        for customer in accounts:
            richman = max(richman, sum(customer))
        return richman

print(Solution().maximumWealth(accounts = [[1,2,3],[3,2,1]]))
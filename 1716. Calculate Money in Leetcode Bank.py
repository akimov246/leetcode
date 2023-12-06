class Solution:
    def totalMoney(self, n: int) -> int:
        bank = 0
        monday = 0
        for day in range(n):
            if day % 7 == 0:
                monday += 1
                counter = 0
            bank += monday + counter
            counter += 1

        return bank


print(Solution().totalMoney(20))
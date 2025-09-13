class Solution:
    def convertDateToBinary(self, date: str) -> str:
        return '-'.join(bin(int(d))[2:] for d in date.split('-'))

print(Solution().convertDateToBinary(date = "2080-02-29"))
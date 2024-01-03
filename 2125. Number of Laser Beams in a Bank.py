from functools import cache

class Solution:
    def numberOfBeams(self, bank: list[str]) -> int:
        if len(bank) == 1:
            return 0
        if bank:
            result = 0
            left = 0
            right = 1
            while left < right and right < len(bank):
                prev = self.sum_of_lasers(bank[left])
                curr = self.sum_of_lasers(bank[right])
                if not prev:
                    left += 1
                    right += 1
                    continue
                if not curr:
                    right += 1
                    continue
                result += prev * curr
                left = right
                right = left + 1
        return result

    @cache
    def sum_of_lasers(self, row: list[str]):
        return sum(int(cell) for cell in row)

# Решение с leetcode
class Solution:
    def numberOfBeams(self, bank: list[str]) -> int:
        ans = 0
        prev = 0
        for row in bank:
            c = row.count('1')
            if c:
                ans += c * prev
                prev = c
        return ans



bank = ["011001","000000","010100","001000"]
print(Solution().numberOfBeams(bank))
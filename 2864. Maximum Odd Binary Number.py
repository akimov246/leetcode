class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        counter = {'0': 0, '1': -1}
        for char in s:
            counter[char] += 1
        return '1' * counter.get('1', 0) + '0' * counter.get('0', 0) + '1'


print(Solution().maximumOddBinaryNumber(s = "010"))
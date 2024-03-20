from sys import set_int_max_str_digits

class Solution:
    def addToArrayForm(self, num: list[int], k: int) -> list[int]:
        set_int_max_str_digits(100000)
        num = [str(n) for n in num]
        ans = str(int("".join(num)) + k)
        return [int(n) for n in ans]


print(Solution().addToArrayForm(num = [1,2,0,0], k = 34))
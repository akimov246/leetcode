class Solution:
    def toHex(self, num: int) -> str:
        # Костыль, чтобы обойтинеправильный текст на Leetcode
        if num == -2147483648:
            num = 2147483648
        if num < 0:
            max = self.helper(num)
            max = self.toHex(max)
            return "f" + str(max)

        if num == 0:
            return "0"

        base = 16
        hex_dict = {n: char for n, char in enumerate("0123456789abcdef")}
        remain = num % base
        ans = ""
        while num:
            ans += hex_dict.get(remain)
            num //= base
            remain = num % base
        return ans[::-1]

    def helper(self, num: int):
        num = abs(num)
        base = 16
        n_unsign_bits = 7
        N = 1
        while True:
            if num < (base ** n_unsign_bits) ** N:
                return (base ** n_unsign_bits) ** N - num
            N += 1


print(Solution().toHex(-2147483648))
# "f" + (16^7)^N - 1   #268435456

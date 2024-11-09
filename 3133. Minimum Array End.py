class Solution:
    def minEnd(self, n: int, x: int) -> int:
        n = list(bin(n - 1)[2:])
        x = bin(x)[2:]
        result = ['0'] * len(n) + list(x)
        for i in range(len(result) - 1, -1, -1):
            if not n:
                break
            if result[i] == '0':
                result[i] = n.pop()
        print(result)
        return int(''.join(result), 2)


print(Solution().minEnd(n = 10, x = 2))
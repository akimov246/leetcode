# Мое решение, хоть и работает, но долговато

class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        # operations = 0
        # bin_n = [True if value == '1' else False for value in bin(n)[2:]]
        # current = [False] * len(bin(n)[2:])
        # while current != bin_n:
        #     if operations % 2:
        #         for i in range(len(current) - 1, -1, -1):
        #             if current[i]:
        #                 current[i - 1] = not current[i - 1]
        #                 break
        #     else:
        #         current[-1] = not current[-1]
        #     operations += 1
        #
        # return operations
        result = n
        while n > 0:
            n >>= 1
            result ^= n
        return result

print(Solution().minimumOneBitOperations(1488))
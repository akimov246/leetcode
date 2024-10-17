class Solution:
    def maximumSwap(self, num: int) -> int:
        num = list(str(num))
        for i in range(len(num) - 1):
            max_idx = num[i + 1:][::-1].index(max(num[i + 1:]))
            if num[i] < num[i + 1:][::-1][max_idx]:
                num[i], num[len(num) - max_idx - 1] = num[len(num) - max_idx - 1], num[i]
                break
        return int(''.join(num))


print(Solution().maximumSwap(num = 98368))
class Solution:
    def minSwaps(self, s: str) -> int:
        swaps = 0
        counter_open = 0
        counter_close = 0
        s = list(s)
        for i, char in enumerate(s):
            if char == '[':
                counter_open += 1
            elif char == ']':
                counter_close += 1
            if counter_close > counter_open:
                x = s[::-1].index('[')
                y = len(s) - 1 - x
                s[i], s[y] = s[y], s[i]
                counter_open += 1
                counter_close -= 1
                swaps += 1

        return swaps


print(Solution().minSwaps(s = "]]][[["))
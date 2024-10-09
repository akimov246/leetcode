class Solution:
    def minSwaps(self, s: str) -> int:
        swaps = 0
        counter_open = 0
        counter_close = 0
        s = list(s)
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] == '[':
                counter_open += 1
            elif s[left] == ']':
                counter_close += 1

            if counter_close > counter_open:
                while s[right] != '[':
                    right -= 1
                s[left], s[right] = s[right], s[left]
                counter_close -= 1
                counter_open += 1
                swaps += 1

            left += 1

        return swaps


print(Solution().minSwaps(s = "]]][[["))
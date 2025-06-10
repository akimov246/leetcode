class Solution:
    def maxDifference(self, s: str) -> int:
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1

        max_freq_odd = 0
        min_freq_even = float('inf')
        for value in freq.values():
            if value % 2:
                max_freq_odd = max(max_freq_odd, value)
            else:
                min_freq_even = min(min_freq_even, value)

        return max_freq_odd - min_freq_even

print(Solution().maxDifference("zgzaaa"))
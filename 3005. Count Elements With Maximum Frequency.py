class Solution:
    def maxFrequencyElements(self, nums: list[int]) -> int:
        num_freq = {}
        for num in nums:
            num_freq[num] = num_freq.get(num, 0) + 1

        freq_amount = {}
        for num in num_freq:
            freq_amount[num_freq[num]] = freq_amount.get(num_freq[num], 0) + num_freq[num]
            
        return freq_amount[max(freq_amount)]

print(Solution().maxFrequencyElements(nums = [1,2,2,3,1,4]))
from collections import defaultdict

class Solution:
    def findShortestSubArray(self, nums: list[int]) -> int:
        val_freq = dict()
        for value in set(nums):
            val_freq[value] = nums.count(value)

        freq_val = defaultdict(list)
        for v, f in val_freq.items():
            freq_val[f].append(v)

        degree = max(freq_val)
        ans = len(nums)

        for value in freq_val[degree]:
            left = nums.index(value)
            right = len(nums) - nums[::-1].index(value)
            ans = min(right - left, ans)

        return ans


print(Solution().findShortestSubArray([1,2,2,3,1,4,2]))
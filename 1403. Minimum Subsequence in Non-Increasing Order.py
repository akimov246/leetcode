class Solution:
    def minSubsequence(self, nums: list[int]) -> list[int]:
        nums.sort()
        subseq = [nums.pop()]
        subseq_sum = subseq[0]
        nums_sum = sum(nums)
        while subseq_sum <= nums_sum:
            element = nums.pop()
            subseq.append(element)
            subseq_sum += element
            nums_sum -= element
        return subseq

print(Solution().minSubsequence(nums = [4,3,10,9,8]))
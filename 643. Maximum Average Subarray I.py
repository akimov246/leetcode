class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        summa = sum(nums[0:k])
        first = nums[0]
        max_avg = summa / k
        for i in range(1, len(nums) - k + 1, 1):
            last = nums[i + k - 1]
            summa -= first
            summa += last
            max_avg = max(max_avg, summa / k)
            first = nums[i]
        return max_avg

print(Solution().findMaxAverage([9,7,3,5,6,2,0,8,1,9], k = 6))
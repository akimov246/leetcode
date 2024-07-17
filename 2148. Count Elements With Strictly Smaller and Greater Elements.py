class Solution:
    def countElements(self, nums: list[int]) -> int:
        min_ = float('inf')
        max_ = -float('inf')
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
            min_ = min(min_, num)
            max_ = max(max_, num)

        return len(nums) - counter[max_] - counter[min_] if min_ == max_ else len(nums)


print(Solution().countElements(nums = [11,7,2,15]))
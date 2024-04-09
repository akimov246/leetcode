class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        res = []
        cache = {}
        for num in nums:
            if cache.get(num, 0):
                smaller = cache[num]
            else:
                smaller = 0
                for n in nums:
                    if n < num:
                        smaller += 1
                cache[num] = smaller
            res.append(smaller)
        return res

print(Solution().smallerNumbersThanCurrent(nums = [8,1,2,2,3]))
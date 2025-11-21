class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        sorted_nums = sorted(nums)
        result = []
        cache = {}
        for n in nums:
            i = cache.get(n)
            if i is None:
                i = sorted_nums.index(n)
                cache[n] = i
            result.append(i)

        return result


print(Solution().smallerNumbersThanCurrent(nums = [8,1,2,2,3]))
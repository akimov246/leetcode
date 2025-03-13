class Solution:
    def minZeroArray(self, nums: list[int], queries: list[list[int]]) -> int:
        if all(num == 0 for num in nums):
            return 0

        diff_array = [0] * (len(nums) + 1)

        for i, (l, r, val) in enumerate(queries, start=1):
            diff_array[l] -= val
            diff_array[r + 1] += val

        diff_sum = 0
        for j in range(len(nums)):
            diff_sum += diff_array[j]
            if max(0, nums[j] + diff_sum) != 0:
                return -1

        diff_array = [0] * (len(nums) + 1)

        for i, (l, r, val) in enumerate(queries, start=1):
            diff_array[l] -= val
            diff_array[r + 1] += val
            diff_sum = 0
            for j in range(len(nums)):
                diff_sum += diff_array[j]
                if max(0, nums[j] + diff_sum) != 0:
                    break
            else:
                return i
        return -1


print(Solution().minZeroArray(nums=[4, 3, 2, 1], queries=[[1, 3, 2], [0, 2, 1]]))

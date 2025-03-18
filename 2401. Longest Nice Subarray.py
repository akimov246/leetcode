class Solution:
    def longestNiceSubarray(self, nums: list[int]) -> int:
        result = 1

        def bitwise_and_is_zero(a, b):
            return not a & b

        def helper(idx, subarray=None, try_this=None):
            a_idx = idx
            b_idx = idx + 1
            if b_idx >= len(nums):
                return try_this
            a = nums[a_idx]
            b = nums[b_idx]
            if try_this is None:
                try_this = []
            if subarray is None:
                subarray = [a]
            if not bitwise_and_is_zero(a, b):
                try_this.append(subarray)
                return try_this
            else:
                subarray.append(b)
                try_this.append(subarray.copy())
                return helper(b_idx, subarray, try_this)

        def check(array):
            for i in range(len(array)):
                for j in range(i + 1, len(array)):
                    if not bitwise_and_is_zero(array[i], array[j]):
                        return False
            return True

        for i in range(len(nums)):
            array = helper(i)
            if array:
                for a in array:
                    if len(a) > result:
                        if check(a):
                            result = len(a)

        return result


print(Solution().longestNiceSubarray(nums = [1,3,8,48,10]))
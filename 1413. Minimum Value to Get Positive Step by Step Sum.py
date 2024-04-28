class Solution:
    def minStartValue(self, nums: list[int]) -> int:
        start_value = 1
        tmp = start_value
        while True:
            is_break = False
            for n in nums:
                tmp += n
                if tmp < 1:
                    start_value += 1
                    tmp = start_value
                    is_break = True
                    break
            if not is_break:
                return start_value

print(Solution().minStartValue(nums = [-3,2,-3,4,2]))
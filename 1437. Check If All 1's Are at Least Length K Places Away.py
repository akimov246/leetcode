class Solution:
    def kLengthApart(self, nums: list[int], k: int) -> bool:
        ones = nums.count(1)
        if not ones:
            return True
        prev_index = nums.index(1)
        for _ in range(1, ones):
            curr_index = nums.index(1, prev_index + 1)
            if curr_index - prev_index <= k:
                return False
            prev_index = curr_index
        return True



print(Solution().kLengthApart(nums = [1,0,0,1,0,1], k = 2))
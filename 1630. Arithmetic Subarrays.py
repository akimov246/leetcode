from typing import List

class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        answer = []
        for i in range(len(l)):
            tmp_nums = nums[l[i]:r[i] + 1]
            tmp_nums.sort()
            answer.append(self.getBoolForSubarray(tmp_nums))
        return answer

    def getBoolForSubarray(self, subarray: List[int]) -> bool:
        if len(subarray) < 2:
            return False

        prev = subarray[0]
        step = subarray[1] - prev
        prev = subarray[1]

        for current in subarray:
            if abs(current - prev) != step:
                return False
            prev = current
        return True




nums = [4,6,5,9,3,7]
l = [0,0,2]
r = [2,3,5]
print(Solution().checkArithmeticSubarrays(nums, l, r))
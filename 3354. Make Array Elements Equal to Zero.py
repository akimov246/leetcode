class Solution:
    def countValidSelections(self, nums: list[int]) -> int:
        valid = 0

        def helper(array, index, direction):
            index += direction
            while 0 <= index < len(array):
                if array[index] == 0:
                    index += direction
                else:
                    array[index] -= 1
                    direction *= -1
                    index += direction

            return not any(n for n in array)

        prev_is_zero = False
        prev_result = 0

        for curr in range(len(nums)):
            if nums[curr] == 0:
                if prev_is_zero:
                    valid += prev_result
                else:
                    prev_is_zero = True
                    right = helper(nums.copy(), curr, 1)
                    left = helper(nums.copy(), curr, -1)
                    prev_result = right + left
                    valid += prev_result
            else:
                prev_is_zero = False

        return valid

print(Solution().countValidSelections(nums = [35,30,33,32,29,31,33,27,30,38,36,31,29,29,32,35,28,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,35,43,33,36,32,34,37,31,41,34,30,37,35,43,36]))
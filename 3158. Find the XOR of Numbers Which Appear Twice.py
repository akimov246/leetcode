class Solution:
    def duplicateNumbersXOR(self, nums: list[int]) -> int:
        twices = set()
        checked = set()
        for num in nums:
            if num in checked:
                twices.add(num)
            checked.add(num)

        result = 0
        for t in twices:
            result ^= t

        return result


print(Solution().duplicateNumbersXOR(nums = [1,2,1,3]))
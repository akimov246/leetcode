class Solution:
    def dominantIndex(self, nums: list[int]) -> int:
        largest = max(set(nums))
        index = nums.index(largest)
        nums.pop(index)
        if max(set(nums)) * 2 <= largest:
            return index
        else:
            return -1

print(Solution().dominantIndex([3,6,1,0]))
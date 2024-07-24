class Solution:
    def mostFrequent(self, nums: list[int], key: int) -> int:
        counter = {}
        for i in range(len(nums) - 1):
            if nums[i] == key:
                counter[nums[i + 1]] = counter.get(nums[i + 1], 0) + 1

        return max(set(counter.items()), key=lambda item: item[1])[0]

print(Solution().mostFrequent(nums = [2,2,2,2,3], key = 2))
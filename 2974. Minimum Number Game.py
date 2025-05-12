class Solution:
    def numberGame(self, nums: list[int]) -> list[int]:
        arr = []
        nums.sort(reverse=True)

        while nums:
            arr.append(nums.pop(-2))
            arr.append(nums.pop())

        return arr

print(Solution().numberGame(nums = [5,4,2,3]))
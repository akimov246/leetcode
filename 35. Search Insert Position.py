class Solution:
    def crutch(self, nums: list[int], target: int) -> int:
        try:
            return nums.index(target)
        except:
            mem = nums[0]
            dist = max(nums)
            for n in nums:
                if abs(n - target) <= dist:
                    dist = abs(n - target)
                    mem = n
            nums.insert(0, min(nums) - 1)
            nums.append(max(nums) + 1)
            if target > mem:
                return nums.index(mem) + 1
            else:
                return nums.index(mem) - 1

    def searchInsert(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            cur = nums[left:right + 1]
            mid = left + (right - left) // 2
            if target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return left




nums = [1, 3, 5, 6]
nums2 = [1, 3, 5, 6]

print(Solution().searchInsert([2, 3, 5, 6], 7))
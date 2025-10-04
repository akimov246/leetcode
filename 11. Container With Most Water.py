class Solution:
    def maxArea(self, height: list[int]) -> int:
        maximum = 0
        left = 0
        right = len(height) - 1

        while left < right:
            maximum = max(maximum, (right - left) * min(height[left], height[right]))
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1

        return maximum


print(Solution().maxArea(height = [1,8,6,2,5,4,8,3,7]))
class Solution:
    def stableMountains(self, height: list[int], threshold: int) -> list[int]:
        stable = []
        for i in range(1, len(height)):
            if height[i - 1] > threshold:
                stable.append(i)

        return stable

print(Solution().stableMountains(height = [1,2,3,4,5], threshold = 2))
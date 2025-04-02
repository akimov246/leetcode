class Solution:
    def findPeaks(self, mountain: list[int]) -> list[int]:
        peaks = []
        for i in range(1, len(mountain) - 1):
            if mountain[i - 1] < mountain[i] > mountain[i + 1]:
                peaks.append(i)

        return peaks

print(Solution().findPeaks(mountain = [1,4,3,8,5]))
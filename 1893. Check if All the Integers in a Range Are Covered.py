class Solution:
    def isCovered(self, ranges: list[list[int]], left: int, right: int) -> bool:
        for x in range(left, right + 1):
            for start, end in ranges:
                if x in range(start, end + 1):
                    break
            else:
                return False
        return True

print(Solution().isCovered(ranges = [[1,2],[3,4],[5,6]], left = 2, right = 7))

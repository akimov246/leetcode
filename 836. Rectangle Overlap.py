class Solution:
    def isRectangleOverlap(self, rec1: list[int], rec2: list[int]) -> bool:
        if rec1[2] <= rec2[0] or rec2[2] <= rec1[0] or rec1[3] <= rec2[1] or rec2[3] <= rec1[1]:
            return False
        return True


print(Solution().isRectangleOverlap(rec1 = [0,0,2,2], rec2 = [1,1,3,3]))



"""
#@@
#@@
"""
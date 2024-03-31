class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        ans = []
        max_ = 0
        for i in range(len(arr) - 1, 0, -1):
            max_ = max(max_, arr[i])
            ans.append(max_)
        ans.reverse()
        ans.append(-1)
        return ans

#print(Solution().replaceElements(arr = [17,18,5,4,6,1]))
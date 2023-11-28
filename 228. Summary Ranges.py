class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        if len(nums) == 1:
            return [str(nums[0])]
        ans = []
        diapson = []
        for num in nums:
            diapson.append(num)
            if num + 1 not in nums:
                ans.append(diapson)
                diapson = []

        result = [f"{ans[i][0]}->{ans[i][-1]}" if ans[i][0] != ans[i][-1] else f"{ans[i][0]}" for i in range(len(ans))]
        return result



print(Solution().summaryRanges([0,1,2,4,5,7]))
#print(Solution().summaryRanges([0]))
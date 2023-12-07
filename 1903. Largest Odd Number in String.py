class Solution:
    def largestOddNumber(self, num: str) -> str:
        ans = ""
        rev_num = num[::-1]
        for i in range(len(rev_num)):
            if int(rev_num[i]) % 2 != 0:
                ans = rev_num[i:][::-1]
                break
        return ans

        # for i in range(len(num) - 1, -1, -1):
        #     if int(num[i]) % 2 != 0:
        #         ans = num[:i + 1]
        #         break
        # return ans





print(Solution().largestOddNumber("4206"))
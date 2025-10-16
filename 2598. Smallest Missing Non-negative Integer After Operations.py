class Solution:
    def findSmallestInteger(self, nums: list[int], value: int) -> int:
        counter = {}
        for i in range(len(nums)):
            n = nums[i] % value
            counter[n] = counter.get(n, 0) + 1

        mex = 0
        while True:
            n = mex % value
            if n in counter:
                counter[n] -= 1
                if counter[n] == 0:
                    counter.pop(n)
            else:
                break
            mex += 1

        return mex


print(Solution().findSmallestInteger(nums = [3,0,3,2,4,2,1,1,0,4], value = 5))
class Solution:
    def sumOddLengthSubarrays(self, arr: list[int]) -> int:
        length = 1
        sum_ = 0
        while length <= len(arr):
            l = 0
            r = length
            for _ in range(r, len(arr) + 1):
                if len(arr[l:r]) < length:
                    break
                sum_ += sum(arr[l:r])
                l += 1
                r += 1
            length += 2
        return sum_

print(Solution().sumOddLengthSubarrays(arr = [1,4,2,5,3]))
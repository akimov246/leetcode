class Solution:
    def findKOr(self, nums: list[int], k: int) -> int:
        max_num_bitmap_length = len(bin(max(nums))[2:])
        bitmap = [bin(n)[2:].rjust(max_num_bitmap_length, '0') for n in nums]
        result = ''
        for bits in zip(*bitmap):
            if bits.count('1') >= k:
                result += '1'
            else:
                result += '0'
        return int(result, 2)

print(Solution().findKOr(nums = [7,12,9,8,9,15], k = 4))
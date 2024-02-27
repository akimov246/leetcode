class Solution:
    def binaryGap(self, n: int) -> int:
        n = bin(n)[2:]
        left = n.find('1')
        right = left + 1
        gap = 0
        if left != -1:
            while left < len(n) and right < len(n):
                if n[right] == '1':
                    gap = max(gap, right - left)
                    left = right
                    right = left + 1
                else:
                    right += 1

        return gap

print(Solution().binaryGap(22))


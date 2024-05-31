class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        first_zero_idx = s.find('0')
        if first_zero_idx != -1:
            if '1' in s[first_zero_idx:]:
                return False
        return True

print(Solution().checkOnesSegment(s = "1001"))
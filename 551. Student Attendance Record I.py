class Solution:
    def checkRecord(self, s: str) -> bool:
        if s.count('A') < 2:
            if s.find('LLL') == -1:
                return True
        return False


print(Solution().checkRecord('PPALLL'))
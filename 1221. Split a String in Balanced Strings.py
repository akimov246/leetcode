class Solution:
    def balancedStringSplit(self, s: str) -> int:
        ans = 0
        while s:
            r_count = 0
            l_count = 0
            for i, char in enumerate(s):
                match char:
                    case 'L':
                        l_count += 1
                    case 'R':
                        r_count += 1
                if l_count == r_count:
                    ans += 1
                    s = s[i + 1:]
                    break
        return ans

print(Solution().balancedStringSplit(s = "RLRRLLRLRL"))
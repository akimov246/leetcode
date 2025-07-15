class Solution:
    def minimumChairs(self, s: str) -> int:
        result = 0
        chairs = 0

        for i in range(len(s)):
            match s[i]:
                case 'E':
                    chairs += 1
                    result = max(result, chairs)
                case 'L':
                    chairs -= 1
        return result

print(Solution().minimumChairs(s = "EEEEEEE"))
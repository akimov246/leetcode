from string import digits

class Solution:
    def clearDigits(self, s: str) -> str:
        result = ''
        for char in s:
            if char in digits:
                result = result[:-1]
            else:
                result += char
                
        return result


print(Solution().clearDigits(s = "cb34"))
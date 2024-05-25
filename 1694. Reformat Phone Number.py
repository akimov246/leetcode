class Solution:
    def reformatNumber(self, number: str) -> str:
        number = number.replace('-', '').replace(' ', '')
        result = []
        while len(number) > 4:
            result.append(number[:3])
            number = number[3:]
        if len(number) in [2, 3]:
            result.append(number)
        elif len(number) == 4:
            result.append(number[:2])
            result.append(number[2:])
        return '-'.join(result)

print(Solution().reformatNumber(number = "1-23-45 6"))
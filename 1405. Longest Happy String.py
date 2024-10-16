class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        result = ''

        letter_number = {
            'a': a,
            'b': b,
            'c': c
        }

        while True:
            current = max(letter_number.items(), key=lambda item: item[1])[0]
            if result and result[-2:] == current * 2:
                tmp = letter_number.copy()
                tmp.pop(current)
                current = max(tmp.items(), key=lambda item: item[1])[0]

            if letter_number[current] == 0:
                return result

            result += current
            letter_number[current] -= 1


print(Solution().longestDiverseString(a = 0, b = 8, c = 11))
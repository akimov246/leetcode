from string import ascii_uppercase

class Solution:
    def cellsInRange(self, s: str) -> list[str]:
        letter_number_map = {letter: number for letter, number in zip(ascii_uppercase, range(1, len(ascii_uppercase) + 1))}
        number_letter_map = {number: letter for number, letter in zip(range(1, len(ascii_uppercase) + 1), ascii_uppercase)}
        col1 = letter_number_map[s[0]]
        row1 = int(s[1])
        col2 = letter_number_map[s[3]]
        row2 = int(s[4])

        cells = []

        for col in range(col1, col2 + 1):
            for row in range(row1, row2 + 1):
                cells.append(number_letter_map[col] + str(row))

        return cells

print(Solution().cellsInRange(s = "K1:L2"))
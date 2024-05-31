class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        letters_to_digits = {letter:digit for letter, digit in zip('abcdefgh', range(1, 9))}
        return True if (letters_to_digits[coordinates[0]] + int(coordinates[1])) % 2 else False

print(Solution().squareIsWhite(coordinates = "a1"))
class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        number = -1
        for word in s.split():
            if word.isdigit():
                if int(word) <= number:
                    return False
                number = int(word)
        return True

print(Solution().areNumbersAscending(s = "1 box has 3 blue 4 red 6 green and 12 yellow marbles"))
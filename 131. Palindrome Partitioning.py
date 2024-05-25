from itertools import zip_longest

class Solution:
    def partition(self, s: str) -> list[list[str]]:

        def is_palidrom(word):
            return word == word[::-1]

        palindromes = [list(s)]
        if len(s) == 1:
            return palindromes

        number_borders = int('1' * (len(s) - 1), 2)
        for border in range(number_borders):
            pattern = bin(border)[2:].rjust((len(s) - 1), '0')
            tmp_s = []
            for char, b in zip_longest(list(s), pattern):
                tmp_s.append(char)
                if b == '1':
                    tmp_s.append('|')
            bordered_s = ''.join(tmp_s).split('|')
            if all(is_palidrom(word) for word in bordered_s):
                print(bordered_s)
                palindromes.append(bordered_s)

        return palindromes




print(Solution().partition('abbcccddddeeeee'))
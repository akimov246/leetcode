class Solution:
    def partition(self, s: str) -> list[list[str]]:

        def is_palidrom(word):
            return word == word[::-1]

        print(bin(3)[2:].rjust(len(s), '0'))

print(Solution().partition('aab'))
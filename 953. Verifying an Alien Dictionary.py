class Solution:
    def isAlienSorted(self, words: list[str], order: str) -> bool:

        def alien_sort(word: str):
                return [order.index(char) for char in word]

        return words == sorted(words, key=alien_sort)



print(Solution().isAlienSorted(words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"))
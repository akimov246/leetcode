class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        first_row = set('qwertyuiop')
        second_row = set('asdfghjkl')
        third_row = set('zxcvbnm')
        ans = []
        for word in words:
            word_set = set(word.lower())
            if word_set.issubset(first_row) \
                or word_set.issubset(second_row) \
                or word_set.issubset(third_row):
                ans.append(word)
        return ans

print(Solution().findWords(["Hello","Alaska","Dad","Peace"]))
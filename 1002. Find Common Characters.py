from collections import Counter

class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        ans = []
        common = set(words[0])
        for i in range(1, len(words)):
            common &= set(words[i])

        longest_word_len = len(max(words, key=len))
        for char in common:
            min_ = longest_word_len
            for word in words:
                min_ = min(min_, word.count(char))
            ans += [char for _ in range(min_)]

        return ans


print(Solution().commonChars(words = ["bella","label","roller"]))
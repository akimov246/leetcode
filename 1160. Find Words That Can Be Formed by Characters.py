from collections import Counter

class Solution:
    def countCharacters(self, words: list[str], chars: str) -> int:
        count = 0
        chars_counter = dict(Counter(chars))
        for word in words:
            if all(word.count(char) <= chars_counter.get(char, 0) for char in set(word)):
                count += len(word)

        return count


print(Solution().countCharacters(words = ["cat","bt","hat","tree"], chars = "atach"))
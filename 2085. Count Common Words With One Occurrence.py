from itertools import zip_longest

class Solution:
    def countWords(self, words1: list[str], words2: list[str]) -> int:
        strings_number = 0
        counter1 = {}
        counter2 = {}
        for word1, word2 in zip_longest(words1, words2):
            if word1:
                counter1[word1] = counter1.get(word1, 0) + 1
            if word2:
                counter2[word2] = counter2.get(word2, 0) + 1
        for word in counter1:
            if counter1[word] == 1 and counter2.get(word, 0) == 1:
                strings_number += 1

        return strings_number

print(Solution().countWords(words1 = ["leetcode","is","amazing","as","is"], words2 = ["amazing","leetcode","is"]))

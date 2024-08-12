from collections import defaultdict

class Solution:
    def oddString(self, words: list[str]) -> str:
        difference = defaultdict(list)

        def get_difference(word):
            diff = []
            for i in range(1, len(word)):
                diff.append(ord(word[i]) - ord(word[i - 1]))
            return tuple(diff)

        for word in words:
            d = get_difference(word)
            difference[d].append(word)
            if len(difference) == 2 and len(difference[d]) > 1:
                difference.pop(d)
                return list(difference.values())[0][0]

        return min(difference.items(), key=lambda item: len(item[1]))[1].pop()


print(Solution().oddString(words = ["dtzca","dtzca","dtzca","yqyyo","dtzca","dtzca"]))
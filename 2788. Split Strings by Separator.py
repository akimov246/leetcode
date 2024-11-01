class Solution:
    def splitWordsBySeparator(self, words: list[str], separator: str) -> list[str]:
        result = []
        for item in words:
            #print(item)
            item = item.split(separator)
            for word in item:
                if word:
                    result.append(word)
        return result

print(Solution().splitWordsBySeparator(words = ["one.two.three","four.five","six"], separator = "."))
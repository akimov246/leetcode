class Solution:
    def replaceWords(self, dictionary: list[str], sentence: str) -> str:
        dictionary.sort(key=len)
        words = sentence.split()
        for i, word in enumerate(words):
            for d in dictionary:
                if word.startswith(d):
                    words[i] = d
                    break
        return ' '.join(words)

print(Solution().replaceWords(dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"))
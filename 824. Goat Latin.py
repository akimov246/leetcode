class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowel = 'aeiouAEIOU'
        words = sentence.split()
        for i in range(len(words)):
            if words[i][0] not in vowel:
                words[i] = words[i][1:] + words[i][0]
            words[i] += 'ma' + 'a' * (i + 1)

        return " ".join(words)




print(Solution().toGoatLatin(sentence = "I speak Goat Latin"))
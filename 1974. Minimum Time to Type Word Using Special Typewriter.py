from string import ascii_lowercase

class Solution:
    def minTimeToType(self, word: str) -> int:
        alphabet = {letter:n for letter, n in zip(ascii_lowercase, range(len(ascii_lowercase)))}
        print(alphabet)
        seconds = 0
        pointer = 'a'
        i = 0
        while i < len(word):
            if word[i] != pointer:
                tmp = (alphabet[pointer] + alphabet[word[i]]) % len(alphabet)
                seconds += (alphabet[pointer] + alphabet[word[i]]) % len(alphabet)
                pointer = word[i]
            else:
                seconds += 1
                i += 1

        return seconds


print(Solution().minTimeToType('bza'))
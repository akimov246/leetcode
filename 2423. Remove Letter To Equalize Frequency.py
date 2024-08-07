class Solution:
    def equalFrequency(self, word: str) -> bool:
        if len(set(word)) == len(word) or len(set(word)) == 1:
            return True
        word = list(word)
        counter = {}
        for char in word:
            counter[char] = counter.get(char, 0) + 1
        if all(value == list(counter.values())[0] for value in counter.values()):
            return False

        for char in set(word):
            counter[char] -= 1
            if counter[char] == 0:
                counter.pop(char)
            if all(value == list(counter.values())[0] for value in counter.values()):
                return True
            counter[char] = counter.get(char, 0) + 1
        return False


print(Solution().equalFrequency(word = "abbcc"))
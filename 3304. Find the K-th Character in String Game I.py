class Solution:
    def kthCharacter(self, k: int) -> str:
        word = 'a'

        while k > len(word):
            generated_string = ''
            for char in word:
                generated_string += chr(ord(char) + 1)
            word += generated_string

        return word[k - 1]

print(Solution().kthCharacter(5))
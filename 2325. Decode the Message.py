from string import ascii_lowercase

class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        table = {}
        index = 0
        for char in key.replace(' ', ''):
            if not table.get(char, False):
                table[char] = ascii_lowercase[index]
                index += 1

        decrypted = ''
        for char in message:
            if table.get(char, False):
                decrypted += table[char]
            else:
                decrypted += char

        return decrypted

print(Solution().decodeMessage(key = "the quick brown fox jumps over the lazy dog", message = "vkbs bs t suepuv"))
from string import ascii_lowercase

class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        letters = ascii_lowercase + 'a'
        letters = {char: letters[letters.index(char) + 1] for char in letters}

        i = 0
        j = 0
        current_str = ''
        while i < len(str1) and j < len(str2):
            if str1[i] == str2[j] or letters[str1[i]] == str2[j]:
                current_str += str2[j]
                j += 1
                if str2 in current_str:
                    return True
            i += 1

        return False

print(Solution().canMakeSubsequence(str1 = "abc", str2 = "ad"))
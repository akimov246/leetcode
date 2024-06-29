class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vowels = 'aeiou'
        counter = 0
        left = 0
        right = 0
        while right <= len(word):
            if right == len(word):
                left += 1
                right = left
                continue
            if word[right] in vowels:
                #dbg = word[left:right + 1]
                if len(set(word[left:right + 1])) == len(vowels):
                    counter += 1
                right += 1
            else:
                left += 1
                right = left

        return counter

print(Solution().countVowelSubstrings(word = "poazaeuioauoiioaouuouaui"))
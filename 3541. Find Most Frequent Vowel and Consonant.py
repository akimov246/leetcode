class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = 'aeiou'
        vowels_frequencies = {}
        consonants_frequencies = {}

        for char in s:
            if char in vowels:
                vowels_frequencies[char] = vowels_frequencies.get(char, 0) + 1
            else:
                consonants_frequencies[char] = consonants_frequencies.get(char, 0) + 1

        return max(vowels_frequencies.values(), default=0) + max(consonants_frequencies.values(), default=0)

print(Solution().maxFreqSum(s = "successes"))
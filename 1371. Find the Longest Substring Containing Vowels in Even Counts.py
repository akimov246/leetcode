class Solution:
    def findTheLongestSubstring(self, s: str) -> int:

        def is_even_vowels(substring: str) -> bool:
            vowels = 'aeiou'
            counter = {}
            for char in substring:
                if char in vowels:
                    counter[char] = counter.get(char, 0) + 1
            for c in counter:
                if counter[c] % 2:
                    return False
            return True

        length = len(s)

        while length:
            for i in range(len(s) + 1 - length):
                if is_even_vowels(s[i:i + length]):
                    return length
            length -= 1

        return length


print(Solution().findTheLongestSubstring(s = "a"))
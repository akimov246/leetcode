class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = 'aeiouAEIOU'
        a_counter = 0
        b_counter = 0
        for a, b in zip(s[:len(s) // 2], s[len(s) // 2:]):
            if a in vowels:
                a_counter += 1
            if b in vowels:
                b_counter += 1
        return a_counter == b_counter

print(Solution().halvesAreAlike('book'))
import string

class Solution:
    def uniqueMorseRepresentations(self, words: list[str]) -> int:
        transformations = set()
        codes = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        morse = {char: code for char, code in zip(string.ascii_lowercase, codes)}
        for word in words:
            t = ""
            for char in word:
                t += morse.get(char)
            transformations.add(t)
        return len(transformations)

print(Solution().uniqueMorseRepresentations(words = ["gin","zen","gig","msg"]))
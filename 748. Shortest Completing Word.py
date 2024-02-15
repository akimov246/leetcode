import string
from collections import defaultdict

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: list[str]) -> str:
        licensePlate = licensePlate.lower()
        words.sort(key=len)
        sift = defaultdict(int)
        for char in licensePlate:
            if char in string.ascii_lowercase:
                sift[char] += 1
        for word in words:
            if all([num <= word.count(char) for char, num in sift.items()]):
                return word

print(Solution().shortestCompletingWord(licensePlate = "1s3 PSt", words = ["step","steps","stripe","stepple"]))
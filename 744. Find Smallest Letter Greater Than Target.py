class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        first = letters[0]
        letters = set(letters)
        letters.add(target)
        letters = sorted(letters)
        idx = letters.index(target) + 1
        return letters[idx] if idx < len(letters) else first

print(Solution().nextGreatestLetter(letters = ["c","f","j"], target = "c"))
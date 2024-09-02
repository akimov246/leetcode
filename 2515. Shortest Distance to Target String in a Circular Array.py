class Solution:
    def closetTarget(self, words: list[str], target: str, startIndex: int) -> int:
        if target not in words:
            return -1
        words1 = (words[startIndex + 1:] + words[:startIndex + 1])[::-1]
        words2 = words[startIndex:] + words[:startIndex]
        for distance, (w1, w2) in enumerate(zip(words1, words2)):
            if w1 == target or w2 == target:
                return distance

print(Solution().closetTarget(words = ["hello","i","am","leetcode","hello"], target = "hello", startIndex = 1))
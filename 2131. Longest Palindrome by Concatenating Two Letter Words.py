class Solution:
    def longestPalindrome(self, words: list[str]) -> int:
        counter = {}

        for word in words:
            counter[word] = counter.get(word, 0) + 1

        diff = 0
        same = 0

        while counter:
            for word in counter:
                if word == word[::-1]:
                    diff += counter[word] // 2 * 4
                    same += counter[word] % 2 * 2
                else:
                    diff += min(counter.get(word, 0), counter.get(word[::-1], 0)) * 4
                counter.pop(word)
                if counter.get(word[::-1]):
                    counter.pop(word[::-1])
                break

        if diff:
            if same:
                return diff + 2
            return diff
        if same:
            return 2
        return 0

print(Solution().longestPalindrome(words = ["ab","ty","yt","lc","cl","ab"]))
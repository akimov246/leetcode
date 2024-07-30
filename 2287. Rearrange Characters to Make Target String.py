class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        t_chars_count = {}
        for char in target:
            t_chars_count[char] = t_chars_count.get(char, 0) + 1
        s_chars_count = {}
        for char in set(target):
            s_chars_count[char] = s.count(char)

        item = min(s_chars_count.items(), key=lambda item: item[1] // t_chars_count[item[0]])
        return item[1] // t_chars_count[item[0]]


print(Solution().rearrangeCharacters(s = "abbaccaddaeea", target = "aaaaa"))
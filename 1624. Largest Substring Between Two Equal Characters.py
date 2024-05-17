class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        max_ = -1
        for char in set(s):
            number_of_current_char = s.count(char)
            if number_of_current_char > 1:
                indexes = []
                start = 0
                for _ in range(number_of_current_char):
                    index = s.find(char, start)
                    indexes.append(index)
                    start = index + 1
                max_ = max(indexes[-1] - indexes[0] - 1, max_)
        return max_


print(Solution().maxLengthBetweenEqualCharacters("mgntdygtxrvxjnwksqhxuxtrv"))
class Solution:
    def reorderSpaces(self, text: str) -> str:
        number_of_spaces = text.count(' ')
        words = text.split()
        if len(words) == 1:
            return ''.join(words) + ' ' * number_of_spaces
        between_spaces = number_of_spaces // (len(words) - 1)
        extra_spaces = number_of_spaces - between_spaces * (len(words) - 1)
        return (' ' * between_spaces).join(words) + ' ' * extra_spaces

print(Solution().reorderSpaces(text = " practice   makes   perfect"))
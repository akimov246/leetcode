class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        name_num_letters = tuple(self.get_number_of_letters(name))
        typed_num_letters = tuple(self.get_number_of_letters(typed))
        if len(name_num_letters) != len(typed_num_letters):
            return False
        for n, t in zip(name_num_letters, typed_num_letters):
            if n > t:
                return False
        return all(name[sum(name_num_letters[:i + 1]) - 1] == typed[sum(typed_num_letters[:i + 1]) - 1] for i in range(len(name_num_letters)))

    def get_number_of_letters(self, text: str) -> list[int]:
        num_letters = []
        left = 0
        right = 0
        nl = 0
        while left < len(text) and right < len(text):
            if text[left] == text[right]:
                nl += 1
                right += 1
                if right >= len(text):
                    num_letters.append(nl)
            else:
                left = right
                num_letters.append(nl)
                nl = 0
        return num_letters


print(Solution().isLongPressedName(name = "saeed", typed = "ssaaedd"))
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        substrings = []
        substrings_number = 0
        for left in range(len(s)):
            if s[left] == '0':
                right = s.find('1', left)
                if right >= 0:
                    group_left = s[left:right]
                else:
                    break
            elif s[left] == '1':
                right = s.find('0', left)
                if right >= 0:
                    group_left = s[left:right]
                else:
                    break

            group_right = s[right:right + len(group_left)]

            if group_left[0] not in group_right and len(group_left) == len(group_right):
                substrings.append(group_left + group_right)
                substrings_number += 1

        return substrings_number

print(Solution().countBinarySubstrings("00110011"))
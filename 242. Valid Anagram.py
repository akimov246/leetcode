import string

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = {char: i for i, char in enumerate(string.ascii_lowercase)}
        for char in s:
            s = s.replace(char, str(letters.get(char)))
            t = t.replace(char, str(letters.get(char)))
        return sorted(list(s)) == sorted(list(t))

# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         s = list(s)
#         for char in t:
#             if char in s:
#                 try:
#                     s.remove(char)
#                 except:
#                     return False
#             else:
#                 return False
#         return True if not s else False


print(Solution().isAnagram("anagram", "nagaram"))

print(Solution().isAnagram("anagram", "nagaram"))


from collections import defaultdict
s = "LeonidAkimov"
count = defaultdict(int)
for char in s:
    count[char] += 1
print(count)
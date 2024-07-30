import string

class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if len(password) < 8:
            return False
        if not any(char in password for char in string.ascii_lowercase):
            return False
        if not any(char in password for char in string.ascii_uppercase):
            return False
        if not any(char in password for char in string.digits):
            return False
        if not any(char in password for char in '!@#$%^&*()-+'):
            return False
        for i in range(2, len(password) + 1, 1):
            if len(set(password[i-2:i])) == 1:
                return False
        return True

# import re
#
# class Solution:
#     def strongPasswordCheckerII(self, password: str) -> bool:
#         pattern = re.compile('(?!.*(.)\1\1)[0-9a-zA-Z!@#$%^&*()-+]{8,}')
#         return bool(pattern.fullmatch(password))

print(Solution().strongPasswordCheckerII(password = "1abZA!a1a2!bbbb"))
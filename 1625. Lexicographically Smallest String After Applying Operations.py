class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:

        already_was = set()
        answer = s

        def add(current):
            result = ''
            for i in range(len(current)):
                if i % 2:
                    result += str((int(current[i]) + a) % 10)
                else:
                    result += current[i]
            return result

        def rotate(current):
            return current[-b:] + current[:-b]

        def helper(current):
            nonlocal answer
            if current in already_was:
                return
            else:
                already_was.add(current)
                answer = min(answer, current)
            return helper(add(current)) or helper(rotate(current))

        helper(s)

        return answer


print(Solution().findLexSmallestString(s = "43987654", a = 7, b = 3))
from functools import reduce

class Solution:
    def shortestToChar(self, s: str, c: str) -> list[int]:
        target_indexes = sorted(set(index for index in range(len(s)) if s[index] == c))
        answer = []
        distance = len(s)
        for i in range(len(s)):
            answer.append(distance)
            distance = len(s)
            for index in target_indexes:
                d = abs(index - i)
                if d < distance:
                    distance = d
                    continue
                break
        answer.append(distance)
            #answer.append(reduce(min, (abs(i - index) for index in target_indexes)))
        return answer[1:]


print(Solution().shortestToChar(s = "loveleetcode", c = "e"))
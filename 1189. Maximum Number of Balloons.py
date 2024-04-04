class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon = 'balloon'
        counter = dict()
        for char in text:
            if char in balloon:
                counter[char] = counter.get(char, 0) + 1
        ans = 0
        while True:
            for char in balloon:
                if counter.get(char, 0) > 0:
                    counter[char] -= 1
                else:
                    return ans
                if char == 'n':
                    ans += 1


print(Solution().maxNumberOfBalloons(text = "nlaebolko"))
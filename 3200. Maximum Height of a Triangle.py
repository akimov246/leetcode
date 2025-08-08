class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        h1 = 0

        r = red
        b = blue
        while True:
            if h1 % 2:
                r -= h1
                if r < 0:
                    break
            else:
                b -= h1
                if b < 0:
                    break
            h1 += 1
        #print(h1)

        h2 = 0

        r = red
        b = blue
        while True:
            if h2 % 2 == 0:
                r -= h2
                if r < 0:
                    break
            else:
                b -= h2
                if b < 0:
                    break
            h2 += 1

        return max(h1 - 1, h2 - 1)

print(Solution().maxHeightOfTriangle(red = 2, blue = 4))
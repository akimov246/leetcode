class Solution:
    def readBinaryWatch(self, turnedOn: int) -> list[str]:
        ans = []
        #11.11.11.11.11 = 1023 dec (0-1024)
        for i in range(1024):
            if bin(i).count("1") == turnedOn:
                h = i // 64
                m = i % 64
                if h < 12 and m < 60:
                    ans.append(self.time_to_str(h, m))
        return ans

    def time_to_str(self, h, m):
        return f"{h}:{m:0>2}"

print(Solution().readBinaryWatch(2))
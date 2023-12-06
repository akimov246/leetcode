class Solution:
    def readBinaryWatch(self, turnedOn: int) -> list[str]:
        times = [1, 2, 4, 8, 16, 32, 100, 200, 400, 800]
        #11.11.11.11.11 = 1023 dec (0-1024)
        for i in range(1024):
            if bin(i).count("1") == turnedOn:
                print(i, bin(i)[2:])

        test = 479
        print(test // 64)
        print(test % 64)


    def time_to_str(self, h, m):
        return f"{h}:{m:0>2}"

print(Solution().readBinaryWatch(8))
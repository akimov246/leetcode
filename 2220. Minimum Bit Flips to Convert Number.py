class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        if start == goal:
            return 0
        start = bin(start)[2:]
        goal = bin(goal)[2:]
        length = len(max(start, goal, key=len))
        start = start.zfill(length)
        goal = goal.zfill(length)
        #print(start, goal, length)
        bit_flips = 0
        for s, g in zip(start, goal):
            if s != g:
                bit_flips += 1
        return bit_flips

print(Solution().minBitFlips(start = 10, goal = 7))
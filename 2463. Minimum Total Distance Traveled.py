from collections import defaultdict

class Solution:
    def minimumTotalDistance(self, robot: list[int], factory: list[list[int]]) -> int:
        total = float('inf')
        robot.sort()
        factory.sort(key=lambda item: item[0])
        factory = [f[0] for f in factory for _ in range(f[1])]
        print(factory)
        print(robot)

        start = 0
        while start + len(robot) <= len(factory):
            current = 0
            dbg = factory[start:]
            for r, f in zip(robot, factory[start:]):
                current += abs(r - f)
            total = min(total, current)
            start += 1

        return total

print(Solution().minimumTotalDistance(robot = [9,11,99,101], factory = [[10,1],[7,1],[14,1],[100,1],[96,1],[103,1]]))
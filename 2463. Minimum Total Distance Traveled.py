class Solution:
    def minimumTotalDistance(self, robot: list[int], factory: list[list[int]]) -> int:

        def helper(robot, factory, total):
            r = robot.pop()
            tmp_f = []
            for i in range(len(factory)):
                pos = factory[i][0]
                limit = factory[i][1]
                if limit:
                    tmp_f.append(factory[i])
            for i in range(len(tmp_f)):





print(Solution().minimumTotalDistance(robot = [0,4,6], factory = [[2,2],[6,2]]))
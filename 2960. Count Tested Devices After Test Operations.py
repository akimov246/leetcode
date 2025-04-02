class Solution:
    def countTestedDevices(self, batteryPercentages: list[int]) -> int:
        tested_devices = 0

        for i in range(len(batteryPercentages)):
            batteryPercentages[i] = max(0, batteryPercentages[i] - tested_devices)
            if batteryPercentages[i] > 0:
                tested_devices += 1

        return tested_devices


print(Solution().countTestedDevices(batteryPercentages = [1,1,2,1,3]))
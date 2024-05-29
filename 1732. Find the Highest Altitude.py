class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        highest_altitude = 0
        altitude = 0
        for g in gain:
            altitude += g
            highest_altitude = max(highest_altitude, altitude)
        return highest_altitude

print(Solution().largestAltitude(gain = [-5,1,5,0,-7]))
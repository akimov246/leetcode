class Solution:
    def maximumUnits(self, boxTypes: list[list[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda type: type[1], reverse=True)
        total = 0
        for boxes, units in boxTypes:
            if boxes > truckSize:
                total += truckSize * units
                break
            total += boxes * units
            truckSize -= boxes

        return total

print(Solution().maximumUnits(boxTypes = [[1,3],[5,5],[2,5],[4,2]], truckSize = 35))
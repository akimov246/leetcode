class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        distance = 0
        liters_used = 0
        while mainTank:
            mainTank -= 1
            liters_used += 1
            distance += 10
            if liters_used % 5 == 0 and additionalTank:
                additionalTank -= 1
                mainTank += 1

        return distance

print(Solution().distanceTraveled(mainTank = 5, additionalTank = 10))
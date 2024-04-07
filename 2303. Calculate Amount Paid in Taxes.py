class Solution:
    def calculateTax(self, brackets: list[list[int]], income: int) -> float:
        taxes = 0
        paid = 0
        for upper, percent in brackets:
            upped_paid = upper - paid
            if income:
                if upped_paid <= income:
                    taxes += upped_paid * percent / 100
                    income -= upped_paid
                    paid += upped_paid
                else:
                    taxes += income * percent / 100
                    return taxes
        return taxes


print(Solution().calculateTax([[2,7],[3,17],[4,37],[7,6],[9,83],[16,67],[19,29]], income = 18))
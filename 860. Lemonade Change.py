class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        bank5 = []
        bank10 = []
        for bill in bills:
            match bill:
                case 5:
                    bank5.append(5)
                case 10:
                    if len(bank5) > 0:
                        bank5.pop()
                        bank10.append(10)
                    else:
                        return False
                case 20:
                    if len(bank5) > 0 and len(bank10) > 0:
                        bank5.pop()
                        bank10.pop()
                    elif len(bank5) > 2:
                        bank5.pop()
                        bank5.pop()
                        bank5.pop()
                    else:
                        return False
        return True

print(Solution().lemonadeChange(bills = [5,5,5,20,5,5,5,20,5,5,5,10,5,20,10,20,10,20,5,5]))
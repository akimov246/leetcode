class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        if str(purchaseAmount)[-1] in '56789':
            roundedAmount = purchaseAmount + (10 - int(str(purchaseAmount)[-1]))
        else:
            roundedAmount = purchaseAmount - int(str(purchaseAmount)[-1])
        return 100 - roundedAmount


print(Solution().accountBalanceAfterPurchase(9))
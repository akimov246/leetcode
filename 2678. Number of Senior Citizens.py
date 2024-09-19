class Solution:
    def countSeniors(self, details: list[str]) -> int:
        counter = 0
        for d in details:
            if int(d[-4:-2]) > 60:
                counter += 1
        return counter

print(Solution().countSeniors(details = ["7868190130M7522","5303914400F9211","9273338290F4010"]))
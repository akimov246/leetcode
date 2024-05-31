class Solution:
    def countMatches(self, items: list[list[str]], ruleKey: str, ruleValue: str) -> int:
        matches = 0
        for type, color, name in items:
            if (ruleKey == 'type' and ruleValue == type) or \
               (ruleKey == 'color' and ruleValue == color) or \
               (ruleKey == 'name' and ruleValue == name):
                    matches += 1
        return matches

# print(Solution().countMatches(items = [["phone","blue","pixel"],
#                                        ["computer","silver","lenovo"],
#                                        ["phone","gold","iphone"]],
#                                         ruleKey = "color", ruleValue = "silver"))
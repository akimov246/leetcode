from functools import cache

class Solution:
    def mincostTickets(self, days: list[int], costs: list[int]) -> int:
        @cache
        def helper(until, total_cost=0):
            if until >= days[-1]:
                return total_cost
            if total_cost:
                for d in days:
                    if d > until:
                        until = d - 1
                        break

            return min(helper(until + 1, total_cost + costs[0]),
                       helper(until + 7, total_cost + costs[1]),
                       helper(until + 30, total_cost + costs[2]))

        return helper(days[0] - 1)


print(Solution().mincostTickets(days = [3,7,9,11,16,17,20,21,22,23,27,28,30,33,36,37,38,39,44,46,47,52,54,56,57,58,59,61,62,66,67,68,69,73,75,76,77,78,82,84,85,86,89,90,91,93,94,96,97,98,101,104,108,110,112,114,116,117,119,122,123,125,127,128,129,130,133,135,137,139,142,144,145,149,151,154,158,159,161,164,167,172,173,174,176,177,180,181,185,187,190,191,192,193,197,201,202,205,206,208,211,212,217,219,220,221,222,224,225,226,229,230,232,234,237,240,243,245,246,249,252,254,257,258,259,261,262,264,265,267,275,281,282,285,288,289,290,291,293,294,296,297,298,299,302,306,307,309,311,313,314,315,316,317,330,334,335,337,338,339,341,344,345,346,348,349,356,357,361], costs = [30,149,476]))
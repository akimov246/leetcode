class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        month_code = {1: 1,
                       2: 4,
                       3: 4,
                       4: 0,
                       5: 2,
                       6: 5,
                       7: 0,
                       8: 3,
                       9: 6,
                       10: 1,
                       11: 4,
                       12: 6}

        days_code = {0: 'Saturday',
                     1: 'Sunday',
                     2: 'Monday',
                     3: 'Tuesday',
                     4: 'Wednesday',
                     5: 'Thursday',
                     6: 'Friday'}

        def is_leap_year(year):
            if year % 400 == 0:
                return True
            if year % 100 == 0:
                return False
            if year % 4 == 0:
                return True
            return False

        def get_month_code(year, month):
            if is_leap_year(year):
                month_code[1] -= 1
                month_code[2] -= 1
            return month_code[month]

        def get_year_code(year):
            year = str(year)
            ye, ar = year[:2], year[2:]
            if ye == '19':
                return (0 + int(ar) + int(ar) // 4) % 7
            elif ye == '20':
                return (6 + int(ar) + int(ar) // 4) % 7
            elif ye == '21':
                return (4 + int(ar) + int(ar) // 4) % 7

        return days_code[(day + get_month_code(year, month) + get_year_code(year)) % 7]



print(Solution().dayOfTheWeek(day = 31, month = 8, year = 2019))
class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        def is_leap_year(year):
            if year % 400 == 0:
                return True
            if year % 100 == 0:
                return False
            if year % 4 == 0:
                return True
            return False

        months = {'01': 31,
                  '02': 28,
                  '03': 31,
                  '04': 30,
                  '05': 31,
                  '06': 30,
                  '07': 31,
                  '08': 31,
                  '09': 30,
                  '10': 31,
                  '11': 30,
                  '12': 31}

        year1, month1, day1 = [int(d) for d in date1.split('-')]
        year2, month2, day2 = [int(d) for d in date2.split('-')]
        value1 = 1 if month1 > 2 and is_leap_year(year1) else 0
        value2 = 1 if month2 > 2 and is_leap_year(year2) else 0
        for y in range(1971, year1):
            if is_leap_year(y):
                value1 += 366
            else:
                value1 += 365
        for y in range(1971, year2):
            if is_leap_year(y):
                value2 += 366
            else:
                value2 += 365

        for m in months:
            if int(m) == month1:
                value1 += day1
                break
            value1 += months[m]

        for m in months:
            if int(m) == month2:
                value2 += day2
                break
            value2 += months[m]

        return abs(value1 - value2)

print(Solution().daysBetweenDates(date1 = "2020-01-15", date2 = "2019-12-31"))
class Solution:
    def dayOfYear(self, date: str) -> int:
        year, month, day = (int(x) for x in date.split('-'))

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

        if is_leap_year(year):
            months['02'] += 1

        res = 0
        for m in months:
            if int(m) == month:
                res += day
                return res
            res += months[m]



print(Solution().dayOfYear(date = "2019-01-09"))
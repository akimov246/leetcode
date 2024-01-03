class Solution:
    def reformatDate(self, date: str) -> str:

        day, month, year = date.split()
        day = day[:len(day) - 2].rjust(2, '0')
        months_d = {"Jan": '01',
                    "Feb": '02',
                    "Mar": '03',
                    "Apr": '04',
                    "May": '05',
                    "Jun": '06',
                    "Jul": '07',
                    "Aug": '08',
                    "Sep": '09',
                    "Oct": '10',
                    "Nov": '11',
                    "Dec": '12'}
        return f'{year}-{months_d[month]}-{day}'


print(Solution().reformatDate('5th Oct 2052'))
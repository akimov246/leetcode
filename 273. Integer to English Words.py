class Solution:
    def numberToWords(self, num: int) -> str:
        num = str(num)
        if num == '0':
            return 'Zero'

        return self._billions(num)

    def _billions(self, n):
        n = str(int(n))
        if len(n) > 10:
            raise ValueError

        if len(n) == 10:
            billions = ''
            if len(n[:-9]) == 1:
                billions = self._units(n[:-9])
            return (billions + ' Billion ' + self._millions(n[-9:])).strip()
        else:
            return self._millions(n).strip()

    def _millions(self, n):
        n = str(int(n))
        if len(n) > 9:
            raise ValueError

        if len(n) in range(7, 10):
            millions = ''
            if len(n[:-6]) == 1:
                millions = self._units(n[:-6])
            elif len(n[:-6]) == 2:
                millions = self._tens(n[:-6])
            elif len(n[:-6]) == 3:
                millions = self._hundreds(n[:-6])
            return millions + ' Million ' + self._thousands(n[-6:]).strip()
        else:
            return self._thousands(n).strip()

    def _thousands(self, n):
        n = str(int(n))
        if len(n) > 6:
            raise ValueError

        if len(n) in range(4, 7):
            thousands = ''
            if len(n[:-3]) == 1:
                thousands = self._units(n[:-3])
            elif len(n[:-3]) == 2:
                thousands = self._tens(n[:-3])
            elif len(n[:-3]) == 3:
                thousands = self._hundreds(n[:-3])
            return (thousands + ' Thousand ' + self._hundreds(n[-3:])).strip()
        else:
            return self._hundreds(n).strip()

    def _hundreds(self, n):
        n = str(int(n))
        if len(n) > 3:
            raise ValueError

        if len(n) == 3:
            return (self._units(n[0]) + ' Hundred ' + self._tens(n[-2:])).strip()
        else:
            return self._tens(n)

    def _tens(self, n):
        n = str(int(n))
        tens_dict = {'00': '',
                     '10': 'Ten',
                     '11': 'Eleven',
                     '12': 'Twelve',
                     '13': 'Thirteen',
                     '14': 'Fourteen',
                     '15': 'Fifteen',
                     '16': 'Sixteen',
                     '17': 'Seventeen',
                     '18': 'Eighteen',
                     '19': 'Nineteen',
                     '20': 'Twenty',
                     '30': 'Thirty',
                     '40': 'Forty',
                     '50': 'Fifty',
                     '60': 'Sixty',
                     '70': 'Seventy',
                     '80': 'Eighty',
                     '90': 'Ninety'}

        if len(n) > 2:
            raise ValueError

        if len(n) == 2:
            if tens_dict.get(n) or tens_dict.get(n) == '':
                return tens_dict.get(n)
            else:
                return (tens_dict.get(n[0] + '0') + ' ' + self._units(n[1])).strip()
        else:
            return self._units(n).strip()

    def _units(self, n):
        n = str(int(n))
        units_dict = {'1': 'One',
                      '2': 'Two',
                      '3': 'Three',
                      '4': 'Four',
                      '5': 'Five',
                      '6': 'Six',
                      '7': 'Seven',
                      '8': 'Eight',
                      '9': 'Nine'}
        if len(n) == 1:
            return units_dict.get(n, '').strip()
        raise ValueError


print(Solution().numberToWords(1000000000))
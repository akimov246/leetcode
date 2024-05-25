from itertools import zip_longest

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        s_list = list(s)
        result_list = []
        while s_list:
            try:
                for _ in range(numRows):
                    result_list.append(s_list.pop(0))

                number_left_spaces = numRows - 2
                number_right_spaces = 1
                while number_left_spaces > 0:
                    if s_list:
                        for _ in range(number_left_spaces):
                            result_list.append('')
                        result_list.append(s_list.pop(0))
                        for _ in range(number_right_spaces):
                            result_list.append('')
                        number_left_spaces -= 1
                        number_right_spaces += 1
                    else:
                        break
            except IndexError:
                pass
        t_result_list = []
        for i in range(0, len(result_list), numRows):
            t_result_list.append(result_list[i:i + numRows])
        result = ''
        for chars in zip_longest(*t_result_list, fillvalue=''):
            result += ''.join(chars)

        return result




print(Solution().convert(s = "PAYPALISHIRING", numRows = 3))

'''
    1 2 3 4
1   P A Y P
2       A
3     L  
4   I S H I     
5       R
6     I
7   N G  
'''
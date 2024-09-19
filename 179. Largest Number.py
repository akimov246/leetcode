from collections import defaultdict

class Solution:
    def largestNumber(self, nums: list[int]) -> str:

        def my_sort1(value):
            value = str(value).ljust(length, str(value)[-1])
            return tuple(str(value))

        def my_sort2(value):
            value = str(value).ljust(length, str(value)[0])
            return tuple(str(value))

        values = defaultdict(list)
        for n in nums:
            values[str(n)[0]].append(n)

        result = ''
        for v in sorted(values, reverse=True):
            length = len(str(max(values[v])))
            print(list(str(n) for n in sorted(values[v], key=my_sort1, reverse=True)))
            print(list(str(n) for n in sorted(values[v], key=my_sort2, reverse=True)))
            result += max((''.join(str(n) for n in sorted(values[v], key=my_sort1, reverse=True)),
                           ''.join(str(n) for n in sorted(values[v], key=my_sort1, reverse=True)[::-1]),
                          ''.join(str(n) for n in sorted(values[v], key=my_sort2, reverse=True)),
                           ''.join(str(n) for n in sorted(values[v], key=my_sort2, reverse=True)[::-1])))

        return str(int(result))

print(Solution().largestNumber(nums = [4704,6306,9385,7536,3462,4798,5422,5529,8070,6241,9094,7846,663,6221,216,6758,8353,3650,3836,8183,3516,5909,6744,1548,5712,2281,3664,7100,6698,7321,4980,8937,3163,5784,3298,9890,1090,7605,1380,1147,1495,3699,9448,5208,9456,3846,3567,6856,2000,3575,7205,2697,5972,7471,1763,1143,1417,6038,2313,6554,9026,8107,9827,7982,9685,3905,8939,1048,282,7423,6327,2970,4453,5460,3399,9533,914,3932,192,3084,6806,273,4283,2060,5682,2,2362,4812,7032,810,2465,6511,213,2362,3021,2745,3636,6265,1518,8398]))